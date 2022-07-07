# Program which finds and prints all prime numbers in range start_range and end_range.

start_range = int(input())
end_range = int(input())
first_pair_is_prime = False

for first_pair in range(start_range, end_range + 1):
    counter = 0
    for divide in range(1, first_pair + 1):
        # print(f"{first_pair} % {divide} = ", first_pair % divide)
        if first_pair % divide == 0:
            counter += 1
    if counter == 2:
        first_pair_is_prime = True
    if first_pair_is_prime:
        print(first_pair)
        first_pair_is_prime = False
