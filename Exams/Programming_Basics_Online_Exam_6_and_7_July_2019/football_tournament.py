# 	W - Отборът е победител и получава 3 точки
# 	D - Срещата е завършила без победител и отборът получава 1 точка
# 	L - Отборът е загубил срещата и не получава точки

team = input()
matches_count = int(input())
play = True
total_points = 0
win = 0
d = 0
loose = 0
win_percent = 0

if matches_count == 0:
    play = False

if play:
    for match in range(matches_count):
        result = input()
        if result == "W":
            total_points += 3
            win += 1
        elif result == "D":
            total_points += 1
            d += 1
        else:
            loose += 1

    win_percent = win / matches_count * 100

if not play:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"""{team} has won {total_points} points during this season.
Total stats:
## W: {win}
## D: {d}
## L: {loose}
Win rate: {win_percent:.2f}%
""")
