gamer_one = input()
gamer_two = input()
points_first_gamer = 0
points_second_gamer = 0
number_wars = False
winner = ""
winner_points = 0

command_one = input()
while command_one != "End of game":
    command_one = int(command_one)
    command_two = int(input())

    if command_one == "End of game" or command_two == "End of game":
        break

    if command_one == command_two and points_first_gamer == 0 and points_second_gamer == 0:
        command_one = int(input())
        command_two = int(input())

    if command_one > command_two:
        points_first_gamer += (command_one - command_two)
    elif command_one < command_two:
        points_second_gamer += (command_two - command_one)
    else:
        number_wars = True
        command_one = int(input())
        command_two = int(input())
        if command_one > command_two:
            winner = gamer_one
            winner_points = points_first_gamer
        elif command_one < command_two:
            winner = gamer_two
            winner_points = points_second_gamer
        break

    command_one = input()
    if command_one == "End of game":
        break

if number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")
else:
    print(f"{gamer_one} has {points_first_gamer} points")
    print(f"{gamer_two} has {points_second_gamer} points")
