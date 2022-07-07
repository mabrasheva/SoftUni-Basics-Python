from math import ceil

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_duration = 1 / 8 * break_duration
rest_duration = 1 / 4 * break_duration

if break_duration >= lunch_duration + rest_duration + episode_duration:
    remaining_time = ceil(break_duration - (lunch_duration + rest_duration + episode_duration))
    print(f"You have enough time to watch {serial_name} and left with {remaining_time} minutes free time.")
else:
    not_enough = ceil((lunch_duration + rest_duration + episode_duration) - break_duration)
    print(f"You don't have enough time to watch {serial_name}, you need {not_enough} more minutes.")
