budget = float(input())
actors = int(input())
clothes_per_actor = float(input())

decor = budget * 0.10

if actors > 150:
    clothes_per_actor = clothes_per_actor - clothes_per_actor * 0.10

cost = actors * clothes_per_actor + decor

if cost <= budget:
    print("Action!")
    remaining = budget - cost
    print(f"Wingard starts filming with {remaining:.2f} leva left.")
else:
    print("Not enough money!")
    not_enough = cost - budget
    print(f"Wingard needs {not_enough:.2f} leva more.")
