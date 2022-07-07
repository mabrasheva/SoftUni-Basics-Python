budget = float(input())
season = input()  # "summer” or "winter”

destination = ""  # "Bulgaria", "Balkans" or "Europe"
accommodation = ""  # "Camp" or "Hotel
spent_money = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        spent_money = budget * 0.30
    else:
        accommodation = "Hotel"
        spent_money = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        spent_money = budget * 0.40
    else:
        accommodation = "Hotel"
        spent_money = budget * 0.80
else:
    destination = "Europe"
    accommodation = "Hotel"
    spent_money = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{accommodation} - {spent_money:.2f}")
