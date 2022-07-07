name = input()
initial_points = 301
total_points = initial_points
won = False
unsuccessful = 0
successful = 0

command = input()

while command != "Retire":
    points_gain = 0
    points = int(input())
    if command == "Single":
        points_gain = points
    elif command == "Double":
        points_gain = 2 * points
    elif command == "Triple":
        points_gain = 3 * points

    if total_points < points_gain:
        unsuccessful += 1
    else:
        successful += 1

        total_points -= points_gain
        if total_points == 0:
            won = True
            break

    command = input()

if won:
    print(f"{name} won the leg with {successful} shots.")
else:
    print(f"{name} retired after {unsuccessful} unsuccessful shots.")
