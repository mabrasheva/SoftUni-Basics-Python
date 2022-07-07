budget = float(input())
season = input()  # "Summer" or "Winter"
car_class = ""  # "Economy class", "Compact class" or "Luxury class"
car_type = ""  # "Cabrio" or "Jeep"
rent = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        rent = budget * 0.35
    else:
        car_type = "Jeep"
        rent = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        rent = budget * 0.45
    else:
        car_type = "Jeep"
        rent = budget * 0.80
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    rent = budget * 0.90

print(f"{car_class}")
print(f"{car_type} - {rent:.2f}")
