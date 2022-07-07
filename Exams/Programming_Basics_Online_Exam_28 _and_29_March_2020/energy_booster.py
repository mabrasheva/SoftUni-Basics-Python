fruit = input()  # "Watermelon", "Mango", "Pineapple" or "Raspberry"
size = input()  # "small" or "big"
count = int(input())
price = 0
total_price_package = 0

if size == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20
elif size == "big":
    if fruit == "Watermelon":
        price = 28.70
    elif fruit == "Mango":
        price = 19.60
    elif fruit == "Pineapple":
        price = 24.80
    elif fruit == "Raspberry":
        price = 15.20

if size == "small":
    total_price_package = 2 * price
elif size == "big":
    total_price_package = 5 * price

total_price = count * total_price_package

if 400 <= total_price <= 1000:
    total_price = 0.85 * total_price
elif total_price > 1000:
    total_price = 0.50 * total_price

print(f"{total_price:.2f} lv.")
