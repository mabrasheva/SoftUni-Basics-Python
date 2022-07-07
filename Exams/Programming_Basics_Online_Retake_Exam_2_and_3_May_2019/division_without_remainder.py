numbers_count = int(input())
division_of_two = 0
division_of_three = 0
division_of_four = 0

for count in range(numbers_count):
    number = int(input())
    if number % 2 == 0:
        division_of_two += 1
    if number % 3 == 0:
        division_of_three += 1
    if number % 4 == 0:
        division_of_four += 1

percent_division_of_two = division_of_two / numbers_count * 100
percent_division_of_three = division_of_three / numbers_count * 100
percent_division_of_four = division_of_four / numbers_count * 100

print(f"{percent_division_of_two:.2f}%")
print(f"{percent_division_of_three:.2f}%")
print(f"{percent_division_of_four:.2f}%")
