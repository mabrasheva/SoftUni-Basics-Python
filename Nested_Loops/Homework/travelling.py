total_sum = 0

while True:
    destination = input()
    if destination == "End":
        break
    else:
        price = float(input())
        total_sum = 0
        while price > total_sum:
            savings = float(input())
            total_sum += savings
        print(f"Going to {destination}!")
