income = input()
total_sum = 0

while income != "NoMoreMoney":
    income = float(income)
    if income < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {income:.2f}")
    total_sum += income
    income = input()
print(f"Total: {total_sum:.2f}")
