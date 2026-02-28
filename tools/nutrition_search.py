NUTRITION_DB = {
    "banana": {"calories": 89, "protein": 1.1, "fiber": 2.6},
    "rice": {"calories": 130, "protein": 2.7, "fiber": 0.4},
    "egg": {"calories": 78, "protein": 6.3, "fiber": 0.0},
    "eggs": {"calories": 78, "protein": 6.3, "fiber": 0.0},
    "apple": {"calories": 52, "protein": 0.3, "fiber": 2.4},
}

def nutrition_search(food_name: str):
    return NUTRITION_DB.get(food_name.lower())
