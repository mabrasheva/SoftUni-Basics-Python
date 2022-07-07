# ABxyBA
a = int(input())
b = int(input())
total_combinations_count = int(input())
counter = 0
flag = False

for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, a + 1):
            for y in range(1, b + 1):

                counter += 1
                if counter <= total_combinations_count:
                    print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")
                else:
                    flag = True

                if x == a and y == b:
                    flag = True

                else:
                    if A < 55:
                        A += 1
                    else:
                        A = 35
                    if B < 96:
                        B += 1
                    else:
                        B = 64
                if flag:
                    exit()
