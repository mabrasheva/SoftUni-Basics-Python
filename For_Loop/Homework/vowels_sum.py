some_text = input()
total_sum = 0

for character in some_text:
    if character == "a":
        total_sum += 1
    elif character == "e":
        total_sum += 2
    elif character == "i":
        total_sum += 3
    elif character == "o":
        total_sum += 4
    elif character == "u":
        total_sum += 5

print(total_sum)
