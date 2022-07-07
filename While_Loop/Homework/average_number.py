count_numbers = int(input())
total_sum = 0

for i in range(count_numbers):
    number = int(input())
    total_sum += number

average_sum = total_sum / count_numbers
print(f"{average_sum:.2f}")
