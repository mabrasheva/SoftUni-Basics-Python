begin_letter = ord(input())
end_letter = ord(input())
exclude_this_letter = ord(input())
counter = 0

for first_letter in range(begin_letter, end_letter + 1):
    for second_letter in range(begin_letter, end_letter + 1):
        for third_letter in range(begin_letter, end_letter + 1):
            if first_letter != exclude_this_letter and second_letter != exclude_this_letter and third_letter != exclude_this_letter:
                counter += 1
                print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)} ", end="")
print(counter)
