book_wanted = input()
checked_book = input()
book_is_found = False
counter = 0

while checked_book != "No More Books":
    if book_wanted == checked_book:
        book_is_found = True
        break
    counter += 1
    checked_book = input()

if book_is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
