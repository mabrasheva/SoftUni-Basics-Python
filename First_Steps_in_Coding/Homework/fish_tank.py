length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_liters = (length * width * height) / 1000
total_liters = volume_liters * (1 - percent / 100)

print(total_liters)
