location_count = int(input())

for location in range(location_count):
    expected_avg_gold = float(input())
    days = int(input())
    total_gold = 0
    for day in range(days):
        gold = float(input())
        total_gold += gold
    avg_gold = total_gold / days
    if avg_gold >= expected_avg_gold:
        print(f"Good job! Average gold per day: {avg_gold:.2f}.")
    else:
        diff = expected_avg_gold - avg_gold
        print(f"You need {diff:.2f} gold.")
