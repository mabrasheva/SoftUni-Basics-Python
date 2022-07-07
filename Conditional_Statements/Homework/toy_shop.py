tour_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trunks_number = int(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trunks_price = 2

toys_number = puzzles_number + dolls_number + bears_number + minions_number + trunks_number
toys_price = puzzles_number * puzzles_price + dolls_number * dolls_price + bears_number * bears_price + minions_number * minions_price + trunks_number * trunks_price

if toys_number >= 50:
    toys_price = toys_price - toys_price * 0.25

toys_price = toys_price - toys_price * 0.10

if toys_price >= tour_price:
    remaining = toys_price - tour_price
    print(f"Yes! {remaining:.2f} lv left.")
else:
    not_enough = tour_price - toys_price
    print(f"Not enough money! {not_enough:.2f} lv needed.")
