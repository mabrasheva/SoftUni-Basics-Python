initial_count = int(input())
current_count = initial_count
eggs_finished = False
eggs_sold = 0

command = input()

while command != "Close":
    eggs_count = int(input())
    if command == "Buy":
        if eggs_count > current_count:
            eggs_finished = True
            break
        current_count -= eggs_count
        eggs_sold += eggs_count
    elif command == "Fill":
        current_count += eggs_count

    command = input()

if eggs_finished:
    print(f"""Not enough eggs in store!
You can buy only {current_count}.
""")
else:
    print(f"""Store is closed!
{eggs_sold} eggs sold.
""")
