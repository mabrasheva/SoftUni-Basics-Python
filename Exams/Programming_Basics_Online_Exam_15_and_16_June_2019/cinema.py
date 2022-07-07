capacity = int(input())
free_seats = capacity
cinema_is_full = False
ticket_price = 5
total_income = 0

people_count = input()

while people_count != "Movie time!":
    people_count = int(people_count)

    if free_seats < people_count:
        cinema_is_full = True
        break

    if people_count % 3 == 0:
        income = (people_count * ticket_price) - 5
    else:
        income = people_count * ticket_price

    total_income += income

    free_seats -= people_count
    people_count = input()

if cinema_is_full:
    print(f"The cinema is full.")
else:
    print(f"There are {free_seats} seats left in the cinema.")
print(f"Cinema income - {total_income} lv.")
