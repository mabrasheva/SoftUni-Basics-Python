total_sum = int(input())
result = 0
for x1 in range(0, total_sum + 1):
    for x2 in range(0, total_sum + 1):
        for x3 in range(0, total_sum + 1):
            if x1 + x2 + x3 == total_sum:
                result += 1
print(result)
