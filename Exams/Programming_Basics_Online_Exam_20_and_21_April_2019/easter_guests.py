from math import ceil

guests_count = int(input())
budget = int(input())

easter_bread_price = 4
egg_price = 0.45

easter_bread_count = ceil(guests_count / 3)
eggs_count = guests_count * 2

total_price = easter_bread_price * easter_bread_count + egg_price * eggs_count

diff = abs(total_price - budget)
if total_price <= budget:
    print(f'''Lyubo bought {easter_bread_count} Easter bread and {eggs_count} eggs.
He has {diff:.2f} lv. left.''')
else:
    print(f'''Lyubo doesn't have enough money.
He needs {diff:.2f} lv. more.''')
