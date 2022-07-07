days = int(input())
total_food = float(input())
total_eaten_food = 0
eaten_food_dog = 0
eaten_food_cat = 0
total_biscuits = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_eaten_food += (dog_food + cat_food)
    eaten_food_dog += dog_food
    eaten_food_cat += cat_food
    if day % 3 == 0:
        biscuits = 0.10 * (dog_food + cat_food)
        total_biscuits += biscuits

percent_eaten_total_food = (total_eaten_food * 100) / total_food
percent_eaten_food_dog = (eaten_food_dog * 100) / total_eaten_food
percent_eaten_food_cat = (eaten_food_cat * 100) / total_eaten_food
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten_total_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_food_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_food_cat:.2f}% eaten from the cat.")
