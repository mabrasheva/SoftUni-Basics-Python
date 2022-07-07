control = int(input())  # 4 … 144

password_is_found = False
counter_numbers_found = 0
password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control:
                    if a < b and c > d:
                        print(f"{a}{b}{c}{d} ", end="")
                        counter_numbers_found += 1
                        if counter_numbers_found == 4:
                            password_is_found = True
                            password = f"{a}{b}{c}{d}"
print()
if password_is_found:
    print(f"Password: {password}")
else:
    print("No!")
