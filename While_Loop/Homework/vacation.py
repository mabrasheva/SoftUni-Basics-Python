vacation_price = float(input())
total_sum = float(input())
counter_days = 0
counter_days_spend = 0
saved_the_sum = True

while total_sum < vacation_price:
    action = input()  # spend or save
    current_sum = float(input())

    counter_days += 1
    if action == "save":
        total_sum += current_sum
        counter_days_spend = 0
    elif action == "spend":
        counter_days_spend += 1
        total_sum -= current_sum
        if total_sum < 0:
            total_sum = 0
    if counter_days_spend == 5:
        saved_the_sum = False
        break

if saved_the_sum:
    print(f"You saved the money for {counter_days} days.")
else:
    print("You can\'t save the money.")
    print(f"{counter_days}")
