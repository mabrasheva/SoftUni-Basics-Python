flowers_type = input()  # "Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
flowers_count = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

total_price = 0

if flowers_type == "Roses":
    total_price = flowers_count * roses_price
    if flowers_count > 80:
        total_price = total_price * 0.90
elif flowers_type == "Dahlias":
    total_price = flowers_count * dahlias_price
    if flowers_count > 90:
        total_price = total_price * 0.85
elif flowers_type == "Tulips":
    total_price = flowers_count * tulips_price
    if flowers_count > 80:
        total_price = total_price * 0.85
elif flowers_type == "Narcissus":
    total_price = flowers_count * narcissus_price
    if flowers_count < 120:
        total_price = total_price * 1.15
elif flowers_type == "Gladiolus":
    total_price = flowers_count * gladiolus_price
    if flowers_count < 80:
        total_price = total_price * 1.20

diff_budget = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {diff_budget:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff_budget:.2f} leva more.")
