chicken = 10.35
fish = 12.40
vegetarian = 8.15

chicken_number = int(input())
fish_number = int(input())
vegetarian_number = int(input())

total_amount_menus = chicken * chicken_number + fish * fish_number + vegetarian * vegetarian_number
total = total_amount_menus + total_amount_menus * 0.2 + 2.50

print (total)
