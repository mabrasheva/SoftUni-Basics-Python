days = int(input())
hours_count = int(input())
total_price = 0

for day in range(1, days + 1):
    price_per_day = 0
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price_per_hour = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        price_per_day += price_per_hour
    total_price += price_per_day
    print(f"Day: {day} - {price_per_day:.2f} leva")
print(f"Total: {total_price:.2f} leva")
