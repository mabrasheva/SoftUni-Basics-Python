# програма, която да намира сладкаря с най-висок резултат

easter_bread_count = int(input())
max_total_points = 0
winner = ""

for easter_bread in range(easter_bread_count):
    name = input()
    name_total_points = 0

    points = input()
    while points != "Stop":
        points = int(points)
        name_total_points += points

        points = input()

    print(f"{name} has {name_total_points} points.")
    if max_total_points < name_total_points:
        max_total_points = name_total_points
        winner = name
        print(f"{name} is the new number 1!")
print(f"{winner} won competition with {max_total_points} points!")
