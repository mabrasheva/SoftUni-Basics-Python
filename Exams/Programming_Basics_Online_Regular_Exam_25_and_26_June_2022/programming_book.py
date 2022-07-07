# Книгата се състои от 899 страници и 2 корици

price_per_page = float(input())
price_per_cover = float(input())
percent_discount = int(input())
designer_price = float(input())
percent_team = int(input())

price = price_per_page * 899 + price_per_cover * 2
price -= percent_discount / 100 * price
price += designer_price
price -= price * percent_team / 100

print(f"Avtonom should pay {price:.2f} BGN.")
