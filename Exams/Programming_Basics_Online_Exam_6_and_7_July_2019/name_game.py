name = input()
max_points = 0
winner = ""

while name != "Stop":
    points = 0
    for letter in name:
        number = int(input())
        if ord(letter) == number:
            points += 10
        else:
            points += 2
    if max_points <= points:
        max_points = points
        winner = name

    name = input()

print(f"The winner is {winner} with {max_points} points!")
