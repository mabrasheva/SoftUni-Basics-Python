count_groups = int(input())
group_musala = 0
group_monblan = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0
total_count_people = 0

for people in range(count_groups):
    count_people = int(input())
    if count_people <= 5:
        group_musala += count_people
    elif count_people <= 12:
        group_monblan += count_people
    elif count_people <= 25:
        group_kilimanjaro += count_people
    elif count_people <= 40:
        group_k2 += count_people
    else:
        group_everest += count_people
    total_count_people += count_people

percent_musala = group_musala * 100 / total_count_people
percent_monblan = group_monblan * 100 / total_count_people
percent_kilimanjaro = group_kilimanjaro * 100 / total_count_people
percent_k2 = group_k2 * 100 / total_count_people
percent_everest = group_everest * 100 / total_count_people

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
