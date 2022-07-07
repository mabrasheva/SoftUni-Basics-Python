import sys

count_of_numbers = int(input())
biggest = -sys.maxsize

sum_numbers = 0
for number in range(count_of_numbers):
    input_number = int(input())
    if input_number > biggest:
        biggest = input_number
    sum_numbers += input_number
if biggest == sum_numbers - biggest:
    print("Yes")
    print(f"Sum = {abs(biggest)}")
else:
    print("No")
    print(f"Diff = {abs(biggest - (sum_numbers - biggest))}")
