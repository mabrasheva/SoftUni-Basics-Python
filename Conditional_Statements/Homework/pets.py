from math import ceil, floor

days = int(input())
total_food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

needed_food_kg = days * (dog_food_kg + cat_food_kg + turtle_food_gr / 1000)

if needed_food_kg <= total_food_kg:
    food_left_kg = floor(total_food_kg - needed_food_kg)
    print(f"{food_left_kg} kilos of food left.")
else:
    not_enough_food_kg = ceil(needed_food_kg - total_food_kg)
    print(f"{not_enough_food_kg} more kilos of food are needed.")
