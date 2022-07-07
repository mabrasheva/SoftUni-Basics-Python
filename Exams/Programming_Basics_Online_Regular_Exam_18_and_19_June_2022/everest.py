# каква височина е достигнал Атанас и за колко дни е изкачил върха
# ден първи от базов лагер, който е на 5 364 метра, а самият връх е на 8 848м
# максималното време, в което той може да изкачва върха е 5 дни
# Програмата приключва
#    при получаване на командата "END",
#    при достигане на върха(8 848м) или
#    при превишаване на разрешените 5 дни за изкачване.

initial_height = 5364
current_height = initial_height
goal_reached = False

command = input()  # "Yes" / "No"
days = 1

while command != "END":

    if command == "Yes":
        days += 1

    meters = int(input())

    if days > 5:
        break
    else:
        current_height += meters

    if current_height >= 8848:
        goal_reached = True
        break

    command = input()

if goal_reached:
    print(f"Goal reached for {days} days!")
else:
    print(f"""Failed!
{current_height}
""")
