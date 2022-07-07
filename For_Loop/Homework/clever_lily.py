age = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())
number_of_toys = 0
savings = 0

for age in range(1, age + 1):
    if age % 2 == 1:
        number_of_toys += 1
    else:
        savings = savings + (10 * (age / 2)) - 1

total_sum = number_of_toys * price_per_toy + savings

diff_sum = abs(total_sum - price_washing_machine)

if total_sum >= price_washing_machine:
    print(f"Yes! {diff_sum:.2f}")
else:
    print(f"No! {diff_sum:.2f}")
