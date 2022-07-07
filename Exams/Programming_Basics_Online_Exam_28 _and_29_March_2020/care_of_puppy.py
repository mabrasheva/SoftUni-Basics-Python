total_food_kg = int(input())
total_food_gr = total_food_kg * 1000
total_food_eaten = 0

command = input()
while command != "Adopted":
    daily_food_gr = int(command)
    total_food_eaten += daily_food_gr
    command = input()

diff = abs(total_food_gr - total_food_eaten)
if total_food_eaten <= total_food_gr:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
