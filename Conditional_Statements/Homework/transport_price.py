kilometers = int(input())
day_or_night = input()

if kilometers < 20:
    if day_or_night == "day":
        price = 0.70 + (0.79 * kilometers)
    else:
        price = 0.70 + (0.90 * kilometers)
elif 20 <= kilometers < 100:
    price = 0.09 * kilometers
else:
    price = 0.06 * kilometers

print(f"{price:.2f}")
