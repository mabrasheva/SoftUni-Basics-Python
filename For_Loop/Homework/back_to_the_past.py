heritage = float(input())
death_year = int(input())
age = 17

for year in range(1800, death_year + 1):
    if year % 2 == 0:
        heritage -= 12000
        age += 1
    else:
        age += 1
        heritage = heritage - (12000 + 50 * age)

if heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage):.2f} dollars to survive.")
