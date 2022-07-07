from math import floor

number_balls = int(input())
number_red_balls = 0
number_orange_balls = 0
number_yellow_balls = 0
number_white_balls = 0
number_other_balls = 0
total_points = 0
divided_count = 0

for balls in range(number_balls):
    color = input()
    if color == "red":
        number_red_balls += 1
        total_points += 5
    elif color == "orange":
        number_orange_balls += 1
        total_points += 10
    elif color == "yellow":
        number_yellow_balls += 1
        total_points += 15
    elif color == "white":
        number_white_balls += 1
        total_points += 20
    elif color == "black":
        divided_count += 1
        total_points = floor(total_points / 2)
        # total_points //= 2
    else:
        number_other_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {number_red_balls}")
print(f"Orange balls: {number_orange_balls}")
print(f"Yellow balls: {number_yellow_balls}")
print(f"White balls: {number_white_balls}")
print(f"Other colors picked: {number_other_balls}")
print(f"Divides from black balls: {divided_count}")
