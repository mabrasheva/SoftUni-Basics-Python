# Един пакет захар е 950 грама, а един пакет брашно е 750 грама.
# колко пакета захар и брашно трябва да купи Деси
# кое е най-голямото количество захар и брашно, които са използвани.

from math import ceil

easter_bread_count = int(input())
max_flour = 0
max_sugar = 0
total_sugar = 0
total_flour = 0

for easter_bread in range(easter_bread_count):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if max_sugar < sugar:
        max_sugar = sugar
    if max_flour < flour:
        max_flour = flour

packages_sugar = ceil(total_sugar / 950)
packages_flour = ceil(total_flour / 750)

print(f"""Sugar: {packages_sugar}
Flour: {packages_flour}
Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.
""")
