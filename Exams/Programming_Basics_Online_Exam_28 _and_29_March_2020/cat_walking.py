minutes_per_one_walk = int(input())
count_of_walks = int(input())
calories_taken = int(input())

total_minutes_walk = count_of_walks * minutes_per_one_walk
calories_burn = total_minutes_walk * 5

if calories_burn >= 0.5 * calories_taken:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")
