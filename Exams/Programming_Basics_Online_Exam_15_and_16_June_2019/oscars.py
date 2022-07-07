actor_name = input()
points_academy = float(input())
jury_count = int(input())
total_points = points_academy

for jury in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    total_points += (len(jury_name) * jury_points) / 2
    if total_points > 1250.5:
        break

if total_points > 1250.50:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")
