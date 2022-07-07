from sys import maxsize

count_of_numbers = int(input())

smallest = maxsize
biggest = - maxsize

for number in range(count_of_numbers):
    input_number = int(input())
    if input_number < smallest:
        smallest = input_number
    if input_number > biggest:
        biggest = input_number

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
