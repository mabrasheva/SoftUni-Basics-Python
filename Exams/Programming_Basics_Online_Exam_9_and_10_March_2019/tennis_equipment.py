from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_count = int(input())
sneakers_count = int(input())
sneakers_price = 1 / 6 * tennis_racket_price
tennis_racket_and_sneakers_sum = tennis_racket_price * tennis_racket_count + sneakers_price * sneakers_count
other_equipment_sum = 0.20 * tennis_racket_and_sneakers_sum

total_sum = tennis_racket_and_sneakers_sum + other_equipment_sum

djokovic_sum = floor(1 / 8 * total_sum)
sponsors_sum = ceil(7 / 8 * total_sum)

print(f"Price to be paid by Djokovic {djokovic_sum}")
print(f"Price to be paid by sponsors {sponsors_sum}")
