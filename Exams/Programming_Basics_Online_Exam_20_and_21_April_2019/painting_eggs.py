size = input()  # "Large", "Medium" or "Small"
colour = input()  # "Red", "Green" or "Yellow"
count = int(input())
price = 0

if size == "Large":
    if colour == "Red":
        price = 16
    elif colour == "Green":
        price = 12
    elif colour == "Yellow":
        price = 9
elif size == "Medium":
    if colour == "Red":
        price = 13
    elif colour == "Green":
        price = 9
    elif colour == "Yellow":
        price = 7
elif size == "Small":
    if colour == "Red":
        price = 9
    elif colour == "Green":
        price = 8
    elif colour == "Yellow":
        price = 5

total_sum = 0.65 * (price * count)

print(f"{total_sum:.2f} leva.")
