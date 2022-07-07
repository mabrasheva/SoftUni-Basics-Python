total_food_kg = int(input())
total_food_gr = total_food_kg * 1000

food_eaten_gr = input()
while food_eaten_gr != "Adopted":
    food_eaten_gr = int(food_eaten_gr)
    total_food_gr -= food_eaten_gr
    food_eaten_gr = input()

if total_food_gr >= 0:
    print(f"Food is enough! Leftovers: {total_food_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(total_food_gr)} grams more.")
