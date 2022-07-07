rest_days = int(input())
total_minutes = 30000
work_days = 365 - rest_days

play_time = rest_days * 127 + work_days * 63

if play_time <= total_minutes:
    print("Tom sleeps well")
    less_for_play = total_minutes - play_time
    hours = less_for_play // 60
    minutes = less_for_play % 60
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    more_for_play = play_time - total_minutes
    hours = more_for_play // 60
    minutes = more_for_play % 60
    print(f"{hours} hours and {minutes} minutes more for play")
