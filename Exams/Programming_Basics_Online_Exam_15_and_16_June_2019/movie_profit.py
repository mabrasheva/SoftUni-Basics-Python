name = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
percent_cinema_tax = int(input())
movie_profit_without_tax = days * tickets_count * ticket_price
movie_profit = movie_profit_without_tax - (movie_profit_without_tax * percent_cinema_tax / 100)

print(f"The profit from the movie {name} is {movie_profit:.2f} lv.")
