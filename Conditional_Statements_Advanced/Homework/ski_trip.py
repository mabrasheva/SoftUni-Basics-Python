days_trip = int(input())
accommodation = input()  # "room for one person", "apartment" or "president apartment"
evaluation = input()  # "positive" or "negative"
nights_trip = days_trip - 1

# prices per night:
total_price = 0
price_room_for_one_person = 18.00 * nights_trip
price_apartment = 25.00 * nights_trip
price_president_apartment = 35.00 * nights_trip

if days_trip < 10:
    price_apartment = price_apartment * 0.70
    price_president_apartment = price_president_apartment * 0.90
elif 10 <= days_trip <= 15:
    price_apartment = price_apartment * 0.65
    price_president_apartment = price_president_apartment * 0.85
else:
    price_apartment = price_apartment * 0.50
    price_president_apartment = price_president_apartment * 0.80

if accommodation == "room for one person":
    total_price = price_room_for_one_person
elif accommodation == "apartment":
    total_price = price_apartment
else:
    total_price = price_president_apartment

if evaluation == "positive":
    total_price = total_price * 1.25
else:
    total_price = total_price * 0.90

print(f"{total_price:.2f}")
