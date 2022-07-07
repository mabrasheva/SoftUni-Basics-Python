from math import ceil, floor

magnolia_number = int(input())
hyacinth_number = int(input())
rose_number = int(input())
cactus_number = int(input())
gift_price = float(input())
tax = 0.05

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

budget_before_tax = (magnolia_number * magnolia_price) + (hyacinth_number * hyacinth_price) + (
            rose_number * rose_price) + (cactus_number * cactus_price)
budget = budget_before_tax - (budget_before_tax * tax)

if budget >= gift_price:
    budget_left = floor(budget - gift_price)
    print(f"She is left with {budget_left} leva.")
else:
    budget_not_enough = ceil(gift_price - budget)
    print(f"She will have to borrow {budget_not_enough} leva.")
