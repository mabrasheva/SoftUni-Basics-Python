country = input()  # "Russia", "Bulgaria" or "Italy"
discipline = input()  # "ribbon", "hoop" or "rope"
difficulty = 0
performance = 0

if discipline == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.200
        performance = 9.500
elif discipline == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
    elif country == "Italy":
        difficulty = 9.450
        performance = 9.350
elif discipline == "rope":
    if country == "Russia":
        difficulty = 9.600
        performance = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.700
        performance = 9.150

total = difficulty + performance
points_less = 20 - total
percent = (points_less / 20) * 100

print(f"The team of {country} get {total:.3f} on {discipline}.")
print(f"{percent:.2f}%")
