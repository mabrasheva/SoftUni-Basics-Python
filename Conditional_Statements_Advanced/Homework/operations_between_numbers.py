first_number = int(input())
second_number = int(input())
operator = input()  # "+", "-", "*", "/", "%"
result = 0

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
elif second_number != 0:
    if operator == "/":
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
    if operator == "%":
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")
else:
    print(f"Cannot divide {first_number} by zero")
