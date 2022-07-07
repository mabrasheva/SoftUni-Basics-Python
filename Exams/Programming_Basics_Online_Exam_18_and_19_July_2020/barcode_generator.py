start_range = int(input())
end_range = int(input())

start_range = str(start_range)
end_range = str(end_range)

start_range_first_digit = int(start_range[0])
start_range_second_digit = int(start_range[1])
start_range_third_digit = int(start_range[2])
start_range_fourth_digit = int(start_range[3])

end_range_first_digit = int(end_range[0])
end_range_second_digit = int(end_range[1])
end_range_third_digit = int(end_range[2])
end_range_fourth_digit = int(end_range[3])

for first_digit in range(start_range_first_digit, end_range_first_digit + 1):
    for second_digit in range(start_range_second_digit, end_range_second_digit + 1):
        for third_digit in range(start_range_third_digit, end_range_third_digit + 1):
            for fourth_digit in range(start_range_fourth_digit, end_range_fourth_digit + 1):
                if first_digit % 2 != 0 and \
                        second_digit % 2 != 0 and \
                        third_digit % 2 != 0 and \
                        fourth_digit % 2 != 0:
                    print(f"{first_digit}{second_digit}{third_digit}{fourth_digit} ", end="")
