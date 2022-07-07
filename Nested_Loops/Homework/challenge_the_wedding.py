men = int(input())
women = int(input())
max_tables = int(input())

count_tables = 0
for men_number in range(1, men + 1):
    for women_number in range(1, women + 1):
        count_tables += 1
        if count_tables <= max_tables:
            print(f"({men_number} <-> {women_number}) ", end="")
