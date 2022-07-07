import sys

input_number = input()
min_number = sys.maxsize

while input_number != "Stop":
    if int(input_number) < min_number:
        min_number = int(input_number)
    input_number = input()
if min_number != sys.maxsize:
    print(min_number)
