month = input()  # May, June, July, August, September or October
period = int(input())
accommodation = ""  # Apartment or Studio
price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    price_apartment = 65
    price_studio = 50
    if period > 14:
        price_studio = price_studio * 0.70
    elif period > 7:
        price_studio = price_studio * 0.95
elif month == "June" or month == "September":
    price_apartment = 68.70
    price_studio = 75.20
    if period > 14:
        price_studio = price_studio * 0.80
else:
    price_apartment = 77
    price_studio = 76

if period > 14:
    price_apartment = price_apartment * 0.90

total_price_apartment = price_apartment * period
total_price_studio = price_studio * period

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
