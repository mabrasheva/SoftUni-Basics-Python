from math import floor

name = input()
seasons = int(input())
series = int(input())
normal_series_duration = float(input())
normal_series_duration_with_ads = 1.20 * normal_series_duration

total_time = seasons * series * normal_series_duration_with_ads + (10 * seasons)
print(f"Total time needed to watch the {name} series is {floor(total_time)} minutes.")
