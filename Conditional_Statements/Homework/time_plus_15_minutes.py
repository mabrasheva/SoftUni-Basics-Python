hour = int(input())
minutes = int(input())

minutes += 15

if minutes > 59:
    hour += 1
    minutes = minutes - 60

if hour > 23:
    hour = hour - 24

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
