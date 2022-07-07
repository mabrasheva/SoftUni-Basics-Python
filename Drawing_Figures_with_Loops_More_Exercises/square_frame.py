number = int(input())

print("+ " + (number - 2) * "- " + "+")
for middle in range(number - 2):
    print("| " + (number - 2) * "- " + "|")
print("+ " + (number - 2) * "- " + "+")
