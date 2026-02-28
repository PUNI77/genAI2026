def calorie_calculator(food_items):
    total = 0
    for item in food_items:
        total += item.get("calories", 0)
    return total
