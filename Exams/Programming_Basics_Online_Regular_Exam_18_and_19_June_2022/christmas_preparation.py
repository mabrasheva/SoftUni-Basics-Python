paper_count = int(input())
cloth_count = int(input())
glue_count = float(input())
percent_discount = int(input())

paper_price = 5.80
cloth_price = 7.20
glue_price = 1.20

total_price_without_discount = paper_price * paper_count + cloth_price * cloth_count + glue_price * glue_count
total_price = total_price_without_discount - percent_discount / 100 * total_price_without_discount

print(f"{total_price:.3f}")
