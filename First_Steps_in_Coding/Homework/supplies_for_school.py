pens = int(input())
markers = int(input())
detergent = int(input())
discount_percent = int(input())

price_pens = 5.80
price_markers = 7.20
price_detergent = 1.20

total_price_without_discount = pens * price_pens + markers * price_markers + detergent * price_detergent
total_price_with_discount = total_price_without_discount - discount_percent / 100 * total_price_without_discount

print(total_price_with_discount)
