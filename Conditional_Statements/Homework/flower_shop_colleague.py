import math
magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

magnolia_price = magnolia_count * 3.25
hyacinth_price = hyacinth_count * 4
roses_price = rose_count * 3.50
cactus_price = cactus_count * 8

total_price = magnolia_price + hyacinth_price + roses_price + cactus_price
taxes = total_price * 0.05
total_price_with_taxes = total_price - taxes
sum =abs(gift_price - total_price_with_taxes)

if total_price_with_taxes < gift_price:
    print(f"She will have to borrow {math.ceil(sum)} leva.")
elif total_price_with_taxes >= gift_price:
    print(f"She is left with {math.floor(sum)} leva.")
