word = input()
the_most_powerful_word = ""
max_sum_letters = 0

while word != "End of words":
    sum_letters = 0
    for letter in word:
        sum_letters += ord(letter)

    if word[0] == "a" or word[0] == "e" or word[0] == "i" \
            or word[0] == "o" or word[0] == "u" or word[0] == "y" \
            or word[0] == "A" or word[0] == "E" or word[0] == "I" \
            or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        sum_letters *= len(word)
    else:
        sum_letters = int(sum_letters / len(word))

    if max_sum_letters <= sum_letters:
        max_sum_letters = sum_letters
        the_most_powerful_word = word

    word = input()

print(f"The most powerful word is {the_most_powerful_word} - {max_sum_letters}")
