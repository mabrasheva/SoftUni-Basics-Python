from math import pi

figure = input()

if figure == "square":
    square_side = float(input())
    square_area = square_side ** 2
    print(f"{square_area:.3f}")
elif figure == "rectangle":
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    rectangle_area = rectangle_side_a * rectangle_side_b
    print(f"{rectangle_area:.3f}")
elif figure == "circle":
    circle_radius = float(input())
    circle_area = pi * (circle_radius ** 2)
    print(f"{circle_area:.3f}")
elif figure == "triangle":
    side_triangle = float(input())
    height_triangle = float(input())
    area_triangle = side_triangle * height_triangle / 2
    print(f"{area_triangle:.3f}")
