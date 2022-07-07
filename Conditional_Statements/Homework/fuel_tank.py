fuel = input().lower()
litres = float(input())

if fuel == "diesel" or fuel == "gasoline" or fuel == "gas":
    if litres >= 25:
        print(f"You have enough {fuel}.")
    else:
        print(f"Fill your tank with {fuel}!")
else:
    print("Invalid fuel!")
