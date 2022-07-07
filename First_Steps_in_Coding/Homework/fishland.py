# mackerel - скумрия
# sprat - цаца
# belted bonito - паламуд
# horse mackerel - сафрид

price_mackerel = float(input())
price_sprat = float(input())
kg_belted_bonito = float(input())
kg_horse_mackerel = float(input())
kg_shell = int(input())

price_belted_bonito = price_mackerel + (60 / 100 * price_mackerel)
price_horse_mackerel = price_sprat + (80 / 100 * price_sprat)
price_shell = 7.50

total = price_belted_bonito * kg_belted_bonito + price_horse_mackerel * kg_horse_mackerel + price_shell * kg_shell

print(f"{total:.2f}")