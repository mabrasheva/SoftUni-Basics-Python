movie = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie != "Finish":
    used_seats = 0
    total_seats = int(input())

    while used_seats < total_seats:
        ticket = input()
        if ticket != "End":
            used_seats += 1
            total_tickets += 1
            if ticket == "student":
                student_tickets += 1
            elif ticket == "standard":
                standard_tickets += 1
            elif ticket == "kid":
                kids_tickets += 1
        else:
            break

    percent_full = used_seats / total_seats * 100
    print(f"{movie} - {percent_full:.2f}% full.")

    movie = input()

percent_student_tickets = student_tickets * 100 / total_tickets
percent_standard_tickets = standard_tickets * 100 / total_tickets
percent_kids_tickets = kids_tickets * 100 / total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kids_tickets:.2f}% kids tickets.")
