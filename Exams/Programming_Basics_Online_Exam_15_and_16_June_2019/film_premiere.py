movie = input()  # "John Wick", "Star Wars" or "Jumanji"
packet = input()  # "Drink", "Popcorn" or "Menu"
tickets_count = int(input())
price = 0

if movie == "John Wick":
    if packet == "Drink":
        price = 12
    elif packet == "Popcorn":
        price = 15
    elif packet == "Menu":
        price = 19

elif movie == "Star Wars":
    if packet == "Drink":
        price = 18
    elif packet == "Popcorn":
        price = 25
    elif packet == "Menu":
        price = 30
    if tickets_count >= 4:
        price = 0.70 * price

elif movie == "Jumanji":
    if packet == "Drink":
        price = 9
    elif packet == "Popcorn":
        price = 11
    elif packet == "Menu":
        price = 14
    if tickets_count == 2:
        price = 0.85 * price

total_sum = tickets_count * price

print(f"Your bill is {total_sum:.2f} leva.")
