# програма, която да изчислява каква сметка трябва да плати всеки един клиент на магазина
# всеки клиент закупил четен брой продукти, ще получи 20% отстъпка от крайната цена
# средно по колко пари е похарчил всеки човек.

clients_count = int(input())
items_count = 0
all_clients_total_sum = 0

for client in range(clients_count):
    client_total_sum = 0
    price = 0
    items_count = 0
    item = input()  # "basket", "wreath" or "chocolate bunny"
    while item != "Finish":
        items_count += 1
        if item == "basket":
            price = 1.50
        elif item == "wreath":
            price = 3.80
        elif item == "chocolate bunny":
            price = 7
        client_total_sum += price

        item = input()

    if items_count % 2 == 0:
        client_total_sum = 0.80 * client_total_sum
    all_clients_total_sum += client_total_sum

    print(f"You purchased {items_count} items for {client_total_sum:.2f} leva.")

average_bill_per_client = all_clients_total_sum / clients_count
print(f"Average bill per client is: {average_bill_per_client:.2f} leva.")
