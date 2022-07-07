count_of_numbers = int(input())
p1_count_of_numbers = 0
p2_count_of_numbers = 0
p3_count_of_numbers = 0
p4_count_of_numbers = 0
p5_count_of_numbers = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(count_of_numbers):
    number = int(input())
    if number < 200:
        p1_count_of_numbers += 1
    elif 200 <= number <= 399:
        p2_count_of_numbers += 1
    elif 400 <= number <= 599:
        p3_count_of_numbers += 1
    elif 600 <= number <= 799:
        p4_count_of_numbers += 1
    else:
        p5_count_of_numbers += 1

p1 = p1_count_of_numbers / count_of_numbers * 100
p2 = p2_count_of_numbers / count_of_numbers * 100
p3 = p3_count_of_numbers / count_of_numbers * 100
p4 = p4_count_of_numbers / count_of_numbers * 100
p5 = p5_count_of_numbers / count_of_numbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
