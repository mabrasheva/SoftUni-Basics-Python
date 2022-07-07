width = int(input())
length = int(input())
height = int(input())
total_area = width * length * height
used_area = 0

while used_area < total_area:
    command = input()
    if command == "Done":
        print(f"{total_area - used_area} Cubic meters left.")
        break
    else:
        used_area += int(command)

if total_area <= used_area:
    print(f"No more free space! You need {used_area - total_area} Cubic meters more.")
