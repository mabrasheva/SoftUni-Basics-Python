eggs_count = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
max_eggs_colour = ""

for eggs in range(eggs_count):
    colour = input()  # "red", "orange", "blue", "green"
    if colour == "red":
        red_eggs += 1
        if max_eggs < red_eggs:
            max_eggs = red_eggs
            max_eggs_colour = "red"
    if colour == "orange":
        orange_eggs += 1
        if max_eggs < orange_eggs:
            max_eggs = orange_eggs
            max_eggs_colour = "orange"
    if colour == "blue":
        blue_eggs += 1
        if max_eggs < blue_eggs:
            max_eggs = blue_eggs
            max_eggs_colour = "blue"
    if colour == "green":
        green_eggs += 1
        if max_eggs < green_eggs:
            max_eggs = green_eggs
            max_eggs_colour = "green"

print(f"""Red eggs: {red_eggs}
Orange eggs: {orange_eggs}
Blue eggs: {blue_eggs}
Green eggs: {green_eggs}
Max eggs: {max_eggs} -> {max_eggs_colour}
""")
