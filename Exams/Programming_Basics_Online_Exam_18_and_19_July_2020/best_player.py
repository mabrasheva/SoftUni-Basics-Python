best_player = ""
max_goals = 0
hat_trick = False
best_player_goals = 0

name = input()

while name != "END":
    count_goal = int(input())

    if count_goal > max_goals:
        max_goals = count_goal
        best_player = name
        best_player_goals = count_goal
        if best_player_goals >= 3:
            hat_trick = True

    if count_goal >= 10:
        break

    name = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
