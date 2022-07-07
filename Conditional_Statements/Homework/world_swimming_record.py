from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_per_one_meter_seconds = float(input())

delay = floor((distance_meters / 15)) * 12.5
time_total_seconds = (distance_meters * time_per_one_meter_seconds) + delay

if time_total_seconds >= record_seconds:
    not_enough = time_total_seconds - record_seconds
    print(f"No, he failed! He was {not_enough:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {time_total_seconds:.2f} seconds.")
