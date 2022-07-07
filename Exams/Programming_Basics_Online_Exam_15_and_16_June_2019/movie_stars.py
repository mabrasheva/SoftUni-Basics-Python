budget = float(input())
budget_left = budget
budget_is_finished = False

actor = input()
while actor != "ACTION":
    if len(actor) > 15:
        salary = 0.20 * budget_left
    else:
        salary = float(input())
    budget_left -= salary
    if budget_left <= 0:
        budget_is_finished = True
        break
    actor = input()

if budget_is_finished:
    print(f"We need {abs(budget_left):.2f} leva for our actors.")
else:
    print(f"We are left with {abs(budget_left):.2f} leva.")
