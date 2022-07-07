days = int(input())
total_sum_all_days = 0
days_won = 0
days_lost = 0

for tournaments in range(days):
    total_sum_current_day = 0
    games_won = 0
    games_lost = 0
    sport = input()
    while sport != "Finish":
        result = input()  # "win" or "lose"
        if result == "win":
            total_sum_current_day += 20
            games_won += 1
        else:
            games_lost += 1
        sport = input()
    if games_won > games_lost:
        total_sum_current_day = 1.10 * total_sum_current_day
        days_won += 1
    else:
        days_lost += 1
    total_sum_all_days += total_sum_current_day

if days_won > days_lost:
    total_sum_all_days = 1.20 * total_sum_all_days
    print(f"You won the tournament! Total raised money: {total_sum_all_days:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum_all_days:.2f}")
