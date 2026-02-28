from agents.nutrition_agent import run_nutrition_coach

def main():
    print("=== Personal Healthcare & Nutrition Coach ===")
    user_input = input("Food log (e.g., 2 eggs, 1 banana, 1 cup rice): ").strip()
    if not user_input:
        print("No input provided.")
        return
    result = run_nutrition_coach(user_input)
    print("\n=== FINAL OUTPUT ===")
    print(result)

if __name__ == "__main__":
    main()
