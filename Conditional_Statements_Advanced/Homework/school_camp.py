season = input()  # “Winter”, “Spring” or “Summer”
group = input()  # “boys”, “girls” or “mixed”
students = int(input())
nights = int(input())
price_per_night = 0
sport = ""

if group == "boys" or group == "girls":
    if season == "Winter":
        price_per_night = 9.60
    elif season == "Spring":
        price_per_night = 7.20
    else:
        price_per_night = 15
else:
    if season == "Winter":
        price_per_night = 10
    elif season == "Spring":
        price_per_night = 9.50
    else:
        price_per_night = 20

price_total = students * price_per_night * nights

if students >= 50:
    price_total = price_total * 0.50
elif 20 <= students < 50:
    price_total = price_total * 0.85
elif 10 <= students < 20:
    price_total = price_total * 0.95

if group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    else:
        sport = "Volleyball"
elif group == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    else:
        sport = "Football"
else:
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    else:
        sport = "Swimming"

print(f"{sport} {price_total:.2f} lv.")
