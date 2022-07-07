easter_bread_count = int(input())
package_eggs_count = int(input())
biscuits_kilos = int(input())

easter_bread_price = 3.20
package_eggs_price = 4.35
biscuits_price_per_kilo = 5.40
paint_per_one_egg_price = 0.15

total_price = easter_bread_price * easter_bread_count + package_eggs_price * package_eggs_count + \
              biscuits_price_per_kilo * biscuits_kilos + package_eggs_count * paint_per_one_egg_price * 12
print(f"{total_price:.2f}")
