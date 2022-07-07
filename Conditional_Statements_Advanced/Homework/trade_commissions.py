city = input()
sale = float(input())

if (city == "Sofia" or city == "Varna" or city == "Plovdiv") and sale >= 0:
    commission_percent = 0
    if city == "Sofia":
        if 0 <= sale <= 500:
            commission_percent = 0.05
        if 500 < sale <= 1000:
            commission_percent = 0.07
        if 1000 < sale <= 10000:
            commission_percent = 0.08
        if sale > 10000:
            commission_percent = 0.12
    elif city == "Varna":
        if 0 <= sale <= 500:
            commission_percent = 0.045
        if 500 < sale <= 1000:
            commission_percent = 0.075
        if 1000 < sale <= 10000:
            commission_percent = 0.10
        if sale > 10000:
            commission_percent = 0.13
    elif city == "Plovdiv":
        if 0 <= sale <= 500:
            commission_percent = 0.055
        if 500 < sale <= 1000:
            commission_percent = 0.08
        if 1000 < sale <= 10000:
            commission_percent = 0.12
        if sale > 10000:
            commission_percent = 0.145
    commission = sale * commission_percent
    print(f"{commission:.2f}")
else:
    print("error")