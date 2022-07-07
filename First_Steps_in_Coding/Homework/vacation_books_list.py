total_pages_number = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day = total_pages_number // pages_per_hour // days

print(hours_per_day)
