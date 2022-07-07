start = int(input())
finish = int(input())
magic = int(input())
combination_is_found = False
combination_counter = 0

for first in range(start, finish + 1):
    for second in range(start, finish + 1):
        combination_counter += 1
        if first + second == magic:
            combination_is_found = True
            break
    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{combination_counter} ({first} + {second} = {magic})")
else:
    print(f"{combination_counter} combinations - neither equals {magic}")