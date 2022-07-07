x = float(input())
y = float(input())
h = float(input())

walls_area = ((x * x) * 2 + (x * y) * 2) - (1.2 * 2) - ((1.5 * 1.5) * 2)
green_paint_liters = walls_area / 3.4
roof_area = (x * y) * 2 + (x * h / 2) * 2
red_paint_liters = roof_area / 4.3

print(f"{green_paint_liters:.2f}")
print(f"{red_paint_liters:.2f}")
