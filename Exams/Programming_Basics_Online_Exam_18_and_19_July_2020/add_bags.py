price_luggage_twenty_kg = float(input())
kg_luggage = float(input())
days = int(input())
luggage_count = int(input())
price_luggage = 0

if kg_luggage < 10:
    price_luggage = 0.20 * price_luggage_twenty_kg
elif kg_luggage <= 20:
    price_luggage = 0.50 * price_luggage_twenty_kg
else:
    price_luggage = price_luggage_twenty_kg

if days > 30:
    price_luggage += 0.10 * price_luggage
elif days >= 7:
    price_luggage += 0.15 * price_luggage
else:
    price_luggage += 0.40 * price_luggage

total_price = luggage_count * price_luggage

print(f"The total price of bags is: {total_price:.2f} lv.")
