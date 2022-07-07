book_wanted = input()
checked_book = input()
book_is_found = True
counter = 0

while book_wanted != checked_book:
    if checked_book != "No More Books":
        counter += 1
        checked_book = input()
    else:
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        book_is_found = False
        break

if book_is_found:
    print(f"You checked {counter} books and found it.")
