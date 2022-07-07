chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()  # Spring, Summer, Autumn, Winter
holiday = input()  # Y or N

price_chrysanthemums = 2.00
price_roses = 4.10
price_tulips = 2.50

if season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15

price_total = chrysanthemums * price_chrysanthemums + roses * price_roses + tulips * price_tulips

if holiday == "Y":
    price_total = price_total * 1.15
if tulips > 7 and season == "Spring":
    price_total = price_total * 0.95
if roses >= 10 and season == "Winter":
    price_total = price_total * 0.90
if (chrysanthemums + roses + tulips) > 20:
    price_total = price_total * 0.80

price_total = price_total + 2

print(f"{price_total:.2f}")
