games_count = int(input())
hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

for game in range(games_count):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fornite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

percent_hearthstone = hearthstone_count / games_count * 100
percent_fornite = fornite_count / games_count * 100
percent_overwatch = overwatch_count / games_count * 100
percent_others = others_count / games_count * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
