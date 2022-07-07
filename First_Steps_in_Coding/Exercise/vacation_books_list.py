total_count_pages = int(input())
pager_per_hour = int(input())
days = int(input())

total_hours = total_count_pages // pager_per_hour
hours_per_day = total_hours // days

print(hours_per_day)
