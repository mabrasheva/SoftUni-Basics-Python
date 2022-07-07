last_sector = input()  # (B-Z)
rows_in_first_sector = int(input())
seats_in_odd_row = int(input())
total_seats = 0

for sector in range(65, ord(last_sector) + 1): # A = 65
    if sector > 65:
        rows_in_first_sector += 1
    for row in range(1, rows_in_first_sector + 1):

        seats_number = 0

        if row % 2 != 0:
            seats_number = seats_in_odd_row
        else:
            seats_number = seats_in_odd_row + 2

        for seats in range(97, 97 + seats_number): # a = 97
            total_seats += 1

            print(f"{chr(sector)}{row}{chr(seats)}")

print(total_seats)
