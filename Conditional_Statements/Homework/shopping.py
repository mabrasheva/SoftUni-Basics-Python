budget = float(input())
video_number = int(input())
cpu_number = int(input())
ram_number = int(input())

video_price = 250
cpu_price = 0.35 * (video_number * video_price)
ram_price = 0.10 * (video_number * video_price)

total = video_number * video_price + cpu_number * cpu_price + ram_number * ram_price

if video_number > cpu_number:
    total = total - (0.15 * total)

if budget >= total:
    remaining = budget - total
    print(f"You have {remaining:.2f} leva left!")
else:
    needed = total - budget
    print(f"Not enough money! You need {needed:.2f} leva more!")
