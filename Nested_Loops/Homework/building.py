count_floors = int(input())
count_rooms = int(input())

for floor in range(count_floors, count_floors - 1, -1):
    for room in range(count_rooms):
        print(f"L{floor}{room}", end=" ")
    print()

for floor in range(count_floors - 1, 0, -1):
    if floor % 2 == 1:
        for room in range(count_rooms):
            print(f"A{floor}{room}", end=" ")
        print()
    else:
        for room in range(count_rooms):
            print(f"O{floor}{room}", end=" ")
        print()
