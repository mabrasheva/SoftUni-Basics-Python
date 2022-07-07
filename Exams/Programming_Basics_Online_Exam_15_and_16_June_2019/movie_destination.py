budget = float(input())
destination = input()  # "Dubai", "Sofia" or "London"
season = input()  # "Summer" or "Winter"
days = int(input())
price = 0

if destination == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000
    price = 0.70 * price
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500
    price = 1.25 * price
elif destination == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250

total_sum = days * price

diff = abs(total_sum - budget)
if total_sum <= budget:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
