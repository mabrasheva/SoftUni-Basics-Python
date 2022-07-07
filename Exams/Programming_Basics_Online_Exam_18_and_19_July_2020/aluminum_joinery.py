joinery_count = int(input())
joinery_type = input()  # "90X130" or "100X150" or "130X180" or "200X300"
delivery = input()  # "With delivery" or "Without delivery"
order_is_valid = True

if joinery_count <= 10:
    order_is_valid = False

if joinery_type == "90X130":
    joinery_price = 110
    if joinery_count > 60:
        joinery_price = 0.92 * joinery_price
    elif joinery_count > 30:
        joinery_price = 0.95 * joinery_price
elif joinery_type == "100X150":
    joinery_price = 140
    if joinery_count > 80:
        joinery_price = 0.90 * joinery_price
    elif joinery_count > 40:
        joinery_price = 0.94 * joinery_price
elif joinery_type == "130X180":
    joinery_price = 190
    if joinery_count > 50:
        joinery_price = 0.88 * joinery_price
    elif joinery_count > 20:
        joinery_price = 0.93 * joinery_price
elif joinery_type == "200X300":
    joinery_price = 250
    if joinery_count > 50:
        joinery_price = 0.86 * joinery_price
    elif joinery_count > 25:
        joinery_price = 0.91 * joinery_price

total_sum = joinery_price * joinery_count

if delivery == "With delivery":
    total_sum += 60

if joinery_count > 99:
    total_sum = 0.96 * total_sum

if order_is_valid:
    print(f"{total_sum:.2f} BGN")
else:
    print("Invalid order")
