destination = input()  # "France", "Italy" or "Germany"
period = input()  # "21-23", "24-27" or "28-31"
nights = int(input())
price = 0

if destination == "France":
    if period == "21-23":
        price = 30
    elif period == "24-27":
        price = 35
    elif period == "28-31":
        price = 40
elif destination == "Italy":
    if period == "21-23":
        price = 28
    elif period == "24-27":
        price = 32
    elif period == "28-31":
        price = 39
elif destination == "Germany":
    if period == "21-23":
        price = 32
    elif period == "24-27":
        price = 37
    elif period == "28-31":
        price = 43

total_price = nights * price

print(f"Easter trip to {destination} : {total_price:.2f} leva.")
