count_of_numbers = int(input())
input_number = int(input())
smallest = input_number
biggest = input_number
for number in range(count_of_numbers - 1):
    input_number = int(input())
    if input_number < smallest:
        smallest = input_number
    if input_number > biggest:
        biggest = input_number
print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
