text = input()
for index, character in enumerate(text):
    if index % 2 == 0:
        print(f"Index = {index}, Character = {character}")
