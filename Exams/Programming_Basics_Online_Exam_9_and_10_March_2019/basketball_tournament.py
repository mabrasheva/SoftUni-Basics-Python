name = input()
win = 0
lost = 0
total_match_count = 0

while name != "End of tournaments":
    match_count = int(input())
    total_match_count += match_count
    for count in range(1, match_count + 1):
        desi_points = int(input())
        others_points = int(input())
        diff = abs(desi_points - others_points)
        if desi_points > others_points:
            print(f"Game {count} of tournament {name}: win with {diff} points.")
            win += 1
        else:
            print(f"Game {count} of tournament {name}: lost with {diff} points.")
            lost += 1

    name = input()

percent_win = win / total_match_count * 100
percent_lost = lost / total_match_count * 100

print(f"{percent_win:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")
