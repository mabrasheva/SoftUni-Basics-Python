command = input()
prime_numbers_sum = 0
nonprime_numbers_sum = 0

while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
    else:
        count = 0
        for current_number in range(1, number + 1):
            if number % current_number == 0:
                count += 1
        if count == 2:
            prime_numbers_sum += number
        else:
            nonprime_numbers_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {nonprime_numbers_sum}")
