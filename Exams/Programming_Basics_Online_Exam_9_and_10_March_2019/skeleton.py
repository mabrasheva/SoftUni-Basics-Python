minutes_control = int(input())
seconds_control = int(input())
distance_meters = float(input())
seconds_hundred_meters = int(input())

total_control_seconds = minutes_control * 60 + seconds_control
delay_times = distance_meters / 120
delay_seconds = delay_times * 2.5
racer_result_seconds = (distance_meters / 100) * seconds_hundred_meters - delay_seconds

if racer_result_seconds <= total_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {racer_result_seconds:.3f}.")
else:
    diff = racer_result_seconds - total_control_seconds
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
