w_meters = float(input())
h_meters = float(input())

w_cm = w_meters * 100
h_cm = h_meters * 100

area_w = (h_cm - 100) // 70
area_h = w_cm // 120

seats_number = area_h * area_w - 3

print(seats_number)
