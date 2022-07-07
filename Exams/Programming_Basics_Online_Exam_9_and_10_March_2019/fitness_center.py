total_people = int(input())
count_back = 0
count_chest = 0
count_legs = 0
count_abs = 0
count_protein_shake = 0
count_protein_bar = 0
count_work_out = 0
count_protein = 0

for person in range(total_people):
    activity = input()  # "Back", "Chest", "Legs", "Abs", "Protein shake", "Protein bar"
    if activity == "Back":
        count_back += 1
        count_work_out += 1
    elif activity == "Chest":
        count_chest += 1
        count_work_out += 1
    elif activity == "Legs":
        count_legs += 1
        count_work_out += 1
    elif activity == "Abs":
        count_abs += 1
        count_work_out += 1
    elif activity == "Protein shake":
        count_protein_shake += 1
        count_protein += 1
    elif activity == "Protein bar":
        count_protein_bar += 1
        count_protein += 1

percent_work_out = count_work_out / total_people * 100
percent_protein = count_protein / total_people * 100

print(f"{count_back} - back")
print(f"{count_chest} - chest")
print(f"{count_legs} - legs")
print(f"{count_abs} - abs")
print(f"{count_protein_shake} - protein shake")
print(f"{count_protein_bar} - protein bar")
print(f"{percent_work_out:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")
