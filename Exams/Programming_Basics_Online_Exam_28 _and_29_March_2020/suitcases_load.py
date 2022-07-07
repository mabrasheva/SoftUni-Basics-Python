capacity = float(input())
free_space = capacity
count_suitcases = 0
no_more_space = False
suitcase = input()

while suitcase != "End":

    suitcase = float(suitcase)

    if (count_suitcases + 1) % 3 == 0:
        suitcase = 1.10 * suitcase

    if free_space <= float(suitcase):
        no_more_space = True
        break

    free_space -= suitcase
    count_suitcases += 1

    suitcase = input()

if no_more_space:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {count_suitcases} suitcases loaded.")
