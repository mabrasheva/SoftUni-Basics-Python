k = int(input())
l = int(input())
m = int(input())
n = int(input())
count = 0
# last_possible = False

for first_digit_number_one in range(k, 8 + 1):
    for second_digit_number_one in range(9, l - 1, -1):
        for first_digit_number_two in range(m, 8 + 1):
            for second_digit_number_two in range(9, n - 1, -1):
                if first_digit_number_one % 2 == 0 and first_digit_number_two % 2 == 0 and \
                        second_digit_number_one % 2 != 0 and second_digit_number_two % 2 != 0:

                    number_one = str(first_digit_number_one) + str(second_digit_number_one)
                    number_two = str(first_digit_number_two) + str(second_digit_number_two)

                    if number_one == number_two:
                        print("Cannot change the same player.")
                    else:
                        count += 1
                        print(f"{number_one} - {number_two}")
                        if count == 6:
                            exit()

                    # number_one = int(f"{first_digit_number_one}{second_digit_number_one}")
                    # number_two = int(f"{first_digit_number_two}{second_digit_number_two}")
                    #
                    # if number_one == number_two:
                    #     print("Cannot change the same player.")
                    # else:
                    #     count += 1
                    #     print(f"{number_one} - {number_two}")
                    #     if count == 6:
                    #         exit()