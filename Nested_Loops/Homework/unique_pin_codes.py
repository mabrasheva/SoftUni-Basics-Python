max_digit_first = int(input())
max_digit_second = int(input())
max_digit_third = int(input())

for first in range(1, max_digit_first + 1):
    if first % 2 == 0:

        for second in range(1, max_digit_second + 1):

            for third in range(1, max_digit_third + 1):
                if third % 2 == 0:

                    if second == 2 or second == 3 or second == 5 or second == 7:
                        print(f"{first} {second} {third}")
