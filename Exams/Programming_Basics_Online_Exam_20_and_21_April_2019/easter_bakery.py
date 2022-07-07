flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_count = int(input())
yeast_count = int(input())
sugar_price = 0.75 * flour_price
eggs_price = 1.10 * flour_price
yeast_price = 0.20 * sugar_price

total_price = flour_price * flour_kg + sugar_price * sugar_kg + eggs_price * eggs_count + yeast_price * yeast_count
print(f"{total_price:.2f}")
