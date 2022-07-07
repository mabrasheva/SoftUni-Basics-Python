from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_one_meter_in_seconds = float(input())

total_time_in_seconds_without_delay = distance_in_meters * time_per_one_meter_in_seconds
delay = floor(distance_in_meters / 50) * 30
total_time_in_seconds = total_time_in_seconds_without_delay + delay

if total_time_in_seconds < record_in_seconds:
    print(f"Yes! The new record is {total_time_in_seconds:.2f} seconds.")
else:
    diff = total_time_in_seconds - record_in_seconds
    print(f"No! He was {diff:.2f} seconds slower.")
