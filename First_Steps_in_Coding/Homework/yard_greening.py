meters = float(input())
price_per_meter = 7.61
price_without_discount = meters * price_per_meter
discount_percent = 18 / 100
final_price = price_without_discount - discount_percent * price_without_discount
final_discount = price_without_discount - final_price

print(f"The final price is {final_price} lv.")
print(f"The discount is {final_discount} lv.")
