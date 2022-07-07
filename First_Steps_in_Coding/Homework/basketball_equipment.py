year_tax = int(input())

shoes = year_tax - (0.40 * year_tax)
clothes = shoes - (0.2 * shoes)
ball = 0.25 * clothes
accessories = 0.20 * ball

total_sum = year_tax + shoes + clothes + ball + accessories

print(total_sum)