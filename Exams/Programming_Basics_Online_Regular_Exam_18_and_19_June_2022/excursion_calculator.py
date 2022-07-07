people = int(input())
season = input()  # "spring", "summer", "autumn" or "winter"
price = 0

if people <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.50
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86
else:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        price = 85

if season == "summer":
    price *= 0.85
elif season == "winter":
    price *= 1.08

total_price = people * price

print(f"{total_price:.2f} leva.")
