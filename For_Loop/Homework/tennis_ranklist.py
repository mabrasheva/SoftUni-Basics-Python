from math import floor

tournaments = int(input())
initial_points = int(input())
total_points = initial_points
wins = 0

for stage in range(tournaments):
    stage = input()
    if stage == "W":
        total_points += 2000
        wins += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

average_points_per_tournament = floor((total_points - initial_points) / tournaments)
percent_wins = (wins / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points_per_tournament}")
print(f"{percent_wins:.2f}%")
