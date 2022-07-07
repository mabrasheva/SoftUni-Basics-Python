count_floors = int(input())
count_rooms = int(input())
floor_letter = ""

for current_floor in range(count_floors, 0, -1):
    for current_room in range(count_rooms):
        if current_floor == count_floors:
            floor_letter = "L"
        elif current_floor % 2 == 1:
            floor_letter = "A"
        elif current_floor % 2 == 0:
            floor_letter = "O"
        print(f"{floor_letter}{current_floor}{current_room}", end=" ")
    print()
