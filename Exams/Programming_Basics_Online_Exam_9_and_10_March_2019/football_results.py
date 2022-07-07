first_result = input()
second_result = input()
third_result = input()
won = 0
lost = 0
drawn = 0

if int(first_result[0]) > int(first_result[2]):
    won += 1
elif int(first_result[0]) < int(first_result[2]):
    lost += 1
else:
    drawn += 1

if int(second_result[0]) > int(second_result[2]):
    won += 1
elif int(second_result[0]) < int(second_result[2]):
    lost += 1
else:
    drawn += 1

if int(third_result[0]) > int(third_result[2]):
    won += 1
elif int(third_result[0]) < int(third_result[2]):
    lost += 1
else:
    drawn += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
