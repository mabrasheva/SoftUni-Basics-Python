max_hundreds = int(input())
max_tens = int(input())
max_ones = int(input())

for hundreds in range(1, max_hundreds + 1):
    count = 0
    for tens in range(1, max_tens + 1):
        for ones in range(1, max_ones + 1):
            if hundreds % 2 == 0 and ones % 2 == 0:
                if tens == 2 or tens == 3 or tens == 5 or tens == 7:
                    print(f"{hundreds} {tens} {ones}")
