time_first = int(input())
time_second = int(input())
time_third = int(input())

total_seconds = time_first + time_second + time_third
total_time_minutes = total_seconds // 60
total_time_seconds = total_seconds % 60

if total_time_seconds < 10:
    print(f"{total_time_minutes}:0{total_time_seconds}")
else:
    print(f"{total_time_minutes}:{total_time_seconds}")
