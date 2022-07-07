groups = int(input())
people_count_group1 = 0
people_count_group2 = 0
people_count_group3 = 0
people_count_group4 = 0
people_count_group5 = 0

for people in range(groups):
    people = int(input())
    if people <= 5:
        people_count_group1 += people
    elif 6 <= people <= 12:
        people_count_group2 += people
    elif 13 <= people <= 25:
        people_count_group3 += people
    elif 26 <= people <= 40:
        people_count_group4 += people
    else:
        people_count_group5 += people

all_people_count = people_count_group1 + people_count_group2 + people_count_group3 + people_count_group4 + people_count_group5
percent_group1 = people_count_group1 / all_people_count * 100
percent_group2 = people_count_group2 / all_people_count * 100
percent_group3 = people_count_group3 / all_people_count * 100
percent_group4 = people_count_group4 / all_people_count * 100
percent_group5 = people_count_group5 / all_people_count * 100
print(f"{percent_group1:.2f}%")
print(f"{percent_group2:.2f}%")
print(f"{percent_group3:.2f}%")
print(f"{percent_group4:.2f}%")
print(f"{percent_group5:.2f}%")
