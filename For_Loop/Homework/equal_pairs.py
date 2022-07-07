pairs_count = int(input())
number_one = int(input())
number_two = int(input())
initial_sum = number_one + number_two
max_diff = 0
pair_sum = initial_sum

for count in range(pairs_count - 1):
    number_one = int(input())
    number_two = int(input())
    pair_sum = number_one + number_two

    diff_sum = abs(initial_sum - pair_sum)

    if diff_sum > max_diff:
        max_diff = diff_sum

    initial_sum = pair_sum

if max_diff == 0:
    print(f"Yes, value={pair_sum}")
else:
    print(f"No, maxdiff={max_diff}")
