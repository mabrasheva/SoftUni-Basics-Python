moves = int(input())
result = 0
range_zero = 0
range_one = 0
range_two = 0
range_three = 0
range_four = 0
range_invalid = 0

for move in range(moves):
    number = int(input())
    if 0 <= number <= 9:
        result += 0.20 * number
        range_zero += 1
    elif 10 <= number <= 19:
        result += 0.30 * number
        range_one += 1
    elif 20 <= number <= 29:
        result += 0.40 * number
        range_two += 1
    elif 30 <= number <= 39:
        result += 50
        range_three += 1
    elif 40 <= number <= 50:
        result += 100
        range_four += 1
    else:
        result /= 2
        range_invalid += 1

percent_range_zero = range_zero * 100 / moves
percent_range_one = range_one * 100 / moves
percent_range_two = range_two * 100 / moves
percent_range_three = range_three * 100 / moves
percent_range_four = range_four * 100 / moves
percent_range_invalid = range_invalid * 100 / moves

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_range_zero:.2f}%")
print(f"From 10 to 19: {percent_range_one:.2f}%")
print(f"From 20 to 29: {percent_range_two:.2f}%")
print(f"From 30 to 39: {percent_range_three:.2f}%")
print(f"From 40 to 50: {percent_range_four:.2f}%")
print(f"Invalid numbers: {percent_range_invalid:.2f}%")
