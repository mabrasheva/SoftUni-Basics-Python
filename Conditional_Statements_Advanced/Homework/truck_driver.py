season = input()  # "Spring", "Summer", "Autumn" or "Winter"
kilometers_per_month = float(input())
salary = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = 0.75 * kilometers_per_month * 4
    elif season == "Summer":
        salary = 0.90 * kilometers_per_month * 4
    else:
        salary = 1.05 * kilometers_per_month * 4
elif 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = 0.95 * kilometers_per_month * 4
    elif season == "Summer":
        salary = 1.10 * kilometers_per_month * 4
    else:
        salary = 1.25 * kilometers_per_month * 4
else:
    salary = 1.45 * kilometers_per_month * 4

salary = salary * 0.90

print(f"{salary:.2f}")
