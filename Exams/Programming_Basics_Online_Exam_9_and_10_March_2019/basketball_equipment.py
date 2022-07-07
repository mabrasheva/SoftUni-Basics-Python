tax = int(input())

shoes = 0.60 * tax
clothes = 0.80 * shoes
ball = 0.25 * clothes
accessories = 0.20 * ball

sum = tax + shoes + clothes + ball + accessories
print(f"{sum:.2f}")
