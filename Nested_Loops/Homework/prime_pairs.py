# First scenario:

# from sympy import isprime
#
# first_pair_start = int(input())
# second_pair_start = int(input())
# diff_first_pair = int(input())
# diff_second_pair = int(input())
#
# for first_pair in range(first_pair_start, first_pair_start + diff_first_pair + 1):
#     for second_pair in range(second_pair_start, second_pair_start + diff_second_pair + 1):
#         if isprime(first_pair) and isprime(second_pair):
#             print(f"{first_pair}{second_pair}")

# Second scenario:

first_pair_start = int(input())
second_pair_start = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())
first_pair_end = first_pair_start + diff_first_pair
second_pair_end = second_pair_start + diff_second_pair

first_pair_is_prime = False
second_pair_is_prime = False

for first_pair in range(first_pair_start, first_pair_end + 1):
    counter_first_prime = 0
    for divide_first_pair in range(1, first_pair + 1):
        # print(f"{first_pair} % {divide} = ", first_pair % divide)
        if first_pair % divide_first_pair == 0:
            counter_first_prime += 1
    if counter_first_prime == 2:
        first_pair_is_prime = True
    if first_pair_is_prime:

        for second_pair in range(second_pair_start, second_pair_end + 1):
            counter_second_prime = 0
            for divide_second_pair in range(1, second_pair + 1):
                if second_pair % divide_second_pair == 0:
                    counter_second_prime += 1
            if counter_second_prime == 2:
                second_pair_is_prime = True
            if first_pair_is_prime and second_pair_is_prime:
                print(f"{first_pair}{second_pair}")
                second_pair_is_prime = False
        first_pair_is_prime = False

