import os
import re

from rag.loader import load_guidelines_text
from rag.vector_store import simple_retrieve_context
from tools.nutrition_search import nutrition_search
from tools.calorie_calculator import calorie_calculator
from evaluation.llm_judge import judge_output
from hitl.approval_node import human_approval

GUIDELINE_PDF = os.path.join("data", "nutrition_guidelines.pdf")

def parse_food_log(text: str):
    items = [x.strip().lower() for x in text.split(",") if x.strip()]
    cleaned = []
    for item in items:
        item = re.sub(r"\b\d+\b", "", item).strip()
        item = item.replace("cups", "").replace("cup", "").strip()
        cleaned.append(item)
    return cleaned

def build_recommendation(food_items, nutrition_data, total_calories, context):
    if not context.strip():
        return "I cannot answer from the provided medical guidelines."

    lines = []
    lines.append("Grounded recommendation (based on provided guidelines):")
    lines.append(f"- Foods logged: {', '.join(food_items)}")
    lines.append(f"- Estimated total calories: {total_calories} kcal")

    if any(d and d.get("fiber", 0) < 1 for d in nutrition_data if d):
        lines.append("- Consider adding more fiber-rich foods if your guidelines recommend it.")

    lines.append("")
    lines.append("If you need condition-specific advice, consult a qualified healthcare professional.")
    return "\n".join(lines)

def run_nutrition_coach(user_food_log: str) -> str:
    if not os.path.exists(GUIDELINE_PDF):
        return "Guideline PDF not found. Please add your file at: data/nutrition_guidelines.pdf"

    guidelines_text = load_guidelines_text(GUIDELINE_PDF)
    context = simple_retrieve_context(guidelines_text, user_food_log)

    food_items = parse_food_log(user_food_log)

    nutrition_data = []
    calorie_items = []
    for food in food_items:
        info = nutrition_search(food)
        nutrition_data.append(info)
        if info:
            calorie_items.append({"name": food, "calories": info["calories"]})

    total_calories = calorie_calculator(calorie_items)

    recommendation = build_recommendation(food_items, nutrition_data, total_calories, context)

    verdict = judge_output(recommendation, context)
    if verdict.startswith("UNSAFE"):
        return f"Blocked by safety judge: {verdict}"

    final = human_approval(recommendation)
    return final
