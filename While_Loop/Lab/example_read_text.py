character = "C"
print(ord(character))

number = 67
print(chr(number))

text = "Hello"
new_text = 0
for character in text:
    new_text += ord(character)
print(new_text)

text = "Hello"
new_text = ""
for character in text:
    new_text += str(ord(character))
print(new_text)

