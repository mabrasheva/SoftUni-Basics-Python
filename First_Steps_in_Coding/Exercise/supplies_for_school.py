pen_count = int(input())
marker_count = int(input())
detergent_lt = int(input())
discount_percent = int(input())

# Пакет химикали - 5.80 лв.
# Пакет маркери - 7.20 лв.
# Препарат - 1.20 лв (за литър)

price_pen = pen_count * 5.80
price_markers = marker_count * 7.20
price_detergent = detergent_lt * 1.20

total_price = price_pen + price_markers + price_detergent

price_with_discount = total_price - (total_price * (discount_percent / 100))

print(price_with_discount)
