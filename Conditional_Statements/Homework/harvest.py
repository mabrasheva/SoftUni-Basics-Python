from math import floor
from math import ceil

vineyard = int(input())
grapes_per_meter = float(input())
wine_needed = int(input())
workers = int(input())

grapes = vineyard * grapes_per_meter
wine = 0.4 * grapes / 2.5

if wine >= wine_needed:
    wine = floor(wine)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    wine_left = ceil(wine - wine_needed)
    wine_per_worker = ceil(wine_left / workers)
    print(f"{wine_left} liters left -> {wine_per_worker} liters per person.")
else:
    wine_not_enough = floor(wine_needed - wine)
    print(f"It will be a tough winter! More {wine_not_enough} liters wine needed.")
