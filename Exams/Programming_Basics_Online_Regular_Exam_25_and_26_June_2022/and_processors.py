# Един процесор се изработва за 3 часа.
# един служител работи 8 часа на ден.
# Броят на произведените процесори да бъде закръглен към по-малкото цяло число.
# Един процесор струва 110.10 лв.

processors_goal = int(input())
employees_count = int(input())
working_days = int(input())

working_hours = employees_count * working_days * 8
processors_done = int(working_hours / 3)

diff = abs(processors_done - processors_goal) * 110.10
if processors_done < processors_goal:
    print(f"Losses: -> {diff:.2f} BGN")
else:
    print(f"Profit: -> {diff:.2f} BGN")
