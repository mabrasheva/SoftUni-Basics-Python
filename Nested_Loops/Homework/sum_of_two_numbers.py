begin = int(input())
end = int(input())
magic = int(input())
combinations = 0
combination_exist = False

for first_number in range(begin, end + 1):
    for second_number in range(begin, end + 1):
        combinations += 1
        if first_number + second_number == magic:
            combination_exist = True
            print(f"Combination N:{combinations} ({first_number} + {second_number} = {magic})")
            exit()
if not combination_exist:
    print(f"{combinations} combinations - neither equals {magic}")
