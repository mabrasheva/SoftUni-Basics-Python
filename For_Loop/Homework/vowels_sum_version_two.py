some_text = input()
some_text_length = len(some_text)

total_sum = 0

for character in range(some_text_length):
    if some_text[character] == "a":
        total_sum += 1
    elif some_text[character] == "e":
        total_sum += 2
    elif some_text[character] == "i":
        total_sum += 3
    elif some_text[character] == "o":
        total_sum += 4
    elif some_text[character] == "u":
        total_sum += 5

print(total_sum)
