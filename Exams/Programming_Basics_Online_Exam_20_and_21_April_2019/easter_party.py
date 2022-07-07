guests_count = int(input())
price_per_guest = float(input())
budget = float(input())
cake = 0.10 * budget

if 10 <= guests_count <= 15:
    price_per_guest = 0.85 * price_per_guest
elif 15 < guests_count <= 20:
    price_per_guest = 0.80 * price_per_guest
elif 20 < guests_count:
    price_per_guest = 0.75 * price_per_guest

total_price = guests_count * price_per_guest + cake
diff = abs(total_price - budget)

if total_price <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
