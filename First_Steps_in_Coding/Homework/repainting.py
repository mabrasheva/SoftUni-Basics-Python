nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_nylon = (nylon + 2) * 1.50
price_paint = (paint + 0.10 * paint) * 14.50
price_thinner = thinner * 5.00

total_price_materials = price_nylon + price_paint + price_thinner + 0.40
total_price_workers = total_price_materials * 0.30 * hours
total_price = total_price_materials + total_price_workers

print(total_price)
