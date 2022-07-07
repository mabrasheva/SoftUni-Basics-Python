v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_volume = p1 * h
p2_volume = p2 * h

p1_p2_volume = p1_volume + p2_volume

if v >= p1_p2_volume:
    percent_full = (p1_p2_volume * 100) / v
    p1_percent_full = (p1_volume * 100) / p1_p2_volume
    p2_percent_full = (p2_volume * 100) / p1_p2_volume
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {p1_percent_full:.2f}%. Pipe 2: {p2_percent_full:.2f}%.")
else:
    overflow_litres = p1_p2_volume - v
    print(f"For {h:.2f} hours the pool overflows with {overflow_litres:.2f} liters.")
