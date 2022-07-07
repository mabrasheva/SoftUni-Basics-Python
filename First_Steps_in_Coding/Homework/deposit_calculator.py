deposit = float(input())
period = int(input())
percent_per_year = float(input())

total = deposit + period * ((deposit * percent_per_year / 100) / 12)

print(total)
