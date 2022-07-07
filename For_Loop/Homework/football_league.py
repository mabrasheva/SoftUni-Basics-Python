capacity = int(input())
fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for number in range(fans):
    sector = input()  # "A", "B", "V", "G".
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

percent_fans_a = fans_a * 100 / fans
percent_fans_b = fans_b * 100 / fans
percent_fans_v = fans_v * 100 / fans
percent_fans_g = fans_g * 100 / fans
percent_all_fans = fans * 100 / capacity

print(f"{percent_fans_a:.2f}%")
print(f"{percent_fans_b:.2f}%")
print(f"{percent_fans_v:.2f}%")
print(f"{percent_fans_g:.2f}%")
print(f"{percent_all_fans:.2f}%")
