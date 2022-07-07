import sys

input_number = input()
max_number = -sys.maxsize

while input_number != "Stop":
    if int(input_number) > max_number:
        max_number = int(input_number)
    input_number = input()
if max_number != -sys.maxsize:
    print(max_number)
