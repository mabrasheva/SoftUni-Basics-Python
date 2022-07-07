n_number = int(input())
m_number = int(input())
s_number = int(input())

for number in range(m_number, n_number - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == s_number:
            break
        else:
            print(f"{number}", end=" ")
