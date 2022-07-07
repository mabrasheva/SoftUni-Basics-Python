player_one_count = int(input())
player_two_count = int(input())
player_one_is_out_of_eggs = False
player_two_is_out_of_eggs = False
end_game = False

command = input()
while command != "End":

    if command == "one":
        player_two_count -= 1
    elif command == "two":
        player_one_count -= 1

    if player_one_count == 0:
        player_one_is_out_of_eggs = True
        break
    elif player_two_count == 0:
        player_two_is_out_of_eggs = True
        break
    command = input()

if player_one_is_out_of_eggs:
    print(f"Player one is out of eggs. Player two has {player_two_count} eggs left.")
elif player_two_is_out_of_eggs:
    print(f"Player two is out of eggs. Player one has {player_one_count} eggs left.")
else:
    print(f'''Player one has {player_one_count} eggs left.
Player two has {player_two_count} eggs left.
''')
