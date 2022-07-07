juniors = int(input())
seniors = int(input())
type = input()  # "trail", "cross-country", "downhill" or "road"

tax = 0

if type == "trail":
    tax = juniors * 5.50 + seniors * 7
elif type == "cross-country":
    tax = juniors * 8 + seniors * 9.50
    if (juniors + seniors) >= 50:
        tax = tax * 0.75
elif type == "downhill":
    tax = juniors * 12.25 + seniors * 13.75
elif type == "road":
    tax = juniors * 20 + seniors * 21.50

total = tax * 0.95

print(f"{total:.2f}")
