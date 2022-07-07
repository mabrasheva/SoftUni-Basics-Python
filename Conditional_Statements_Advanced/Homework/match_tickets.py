budget = float(input())
category = input()  # "VIP" или "Normal"
people = int(input())
transport = 0
tickets_price = 0

price_vip = 499.99
price_normal = 249.99

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif 50 <= people:
    transport = budget * 0.25

remaining_budget = budget - transport

if category == "VIP":
    tickets_price = price_vip * people
else:
    tickets_price = price_normal * people

diff_budget = abs(tickets_price - remaining_budget)

if tickets_price <= remaining_budget:
    print(f"Yes! You have {diff_budget:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff_budget:.2f} leva.")
