from math import floor

games_count = int(input())
initial_points = int(input())
points_gain = 0
points = 0
games_won = 0

for games in range(games_count):
    position = input()  # "W", "F" or "SF"

    if position == "W":
        points = 2000
        games_won += 1
    elif position == "F":
        points = 1200
    elif position == "SF":
        points = 720

    points_gain += points

final_points = initial_points + points_gain
average_points = floor(points_gain / games_count)
percent_won = games_won / games_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")
