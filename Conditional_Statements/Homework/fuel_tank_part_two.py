fuel = input()
litres = int(input())
club_card = input()

price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93

if club_card == "Yes":
    if fuel == "Gasoline":
        price = (price_gasoline - 0.18) * litres
    elif fuel == "Diesel":
        price = (price_diesel - 0.12) * litres
    elif fuel == "Gas":
        price = (price_gas - 0.08) * litres
elif club_card == "No":
    if fuel == "Gasoline":
        price = price_gasoline * litres
    elif fuel == "Diesel":
        price = price_diesel * litres
    elif fuel == "Gas":
        price = price_gas * litres

if 20 < litres <= 25:
    price = price - (0.08 * price)
elif litres > 25:
    price = price - (0.10 * price)

print(f"{price:.2f} lv.")
