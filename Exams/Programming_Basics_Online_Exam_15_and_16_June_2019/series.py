budget = float(input())
serials_count = int(input())
expenses = 0

for serial in range(serials_count):
    name = input()
    price = float(input())
    if name == "Thrones":
        price = 0.50 * price
    elif name == "Lucifer":
        price = 0.60 * price
    elif name == "Protector":
        price = 0.70 * price
    elif name == "TotalDrama":
        price = 0.80 * price
    elif name == "Area":
        price = 0.90 * price
    expenses += price

diff = abs(expenses - budget)
if expenses <= budget:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
