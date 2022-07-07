inherited_money = float(input())
year_to_live = int(input())
current_year = 1800
spend_money_per_year = 0
total_money_spent = 0
age = 17
for years in range(current_year, year_to_live + 1):
    if current_year % 2 == 0:
        spend_money_per_year = 12000
        age += 1
    else:
        age += 1
        spend_money_per_year = 12000 + 50 * age
    inherited_money -= spend_money_per_year
    current_year += 1

# diff = abs(inherited_money - total_money_spent)
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(inherited_money):.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")