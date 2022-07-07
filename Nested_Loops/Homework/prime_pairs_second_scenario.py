from sympy import isprime

first_pair_start = int(input())
second_pair_start = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())

for first_pair in range(first_pair_start, first_pair_start + diff_first_pair + 1):
    for second_pair in range(second_pair_start, second_pair_start + diff_second_pair + 1):
        if isprime(first_pair) and isprime(second_pair):
            print(f"{first_pair}{second_pair}")