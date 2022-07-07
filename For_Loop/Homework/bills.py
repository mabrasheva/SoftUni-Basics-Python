number_of_months = int(input())
electricity = 0
water = 20
internet = 15
other = (electricity + water + internet) * 1.20
total_electricity = 0

for number in range(number_of_months):
    electricity = float(input())
    total_electricity += electricity

total_water = water * number_of_months
total_other = (total_electricity + ((water + internet) * number_of_months)) * 1.20
total_internet = internet * number_of_months
total_average_per_month = (total_electricity + total_water + total_internet + total_other) / number_of_months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {total_average_per_month:.2f} lv")
