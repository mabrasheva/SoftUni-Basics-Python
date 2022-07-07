actor_name = input()
academy_points = float(input())
jury_count = int(input())
total_points = academy_points

for number in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    length_jury_name = len(jury_name)

    points = length_jury_name * jury_points / 2
    total_points = total_points + points
    if total_points >= 1250.50:
        break

if total_points < 1250.50:
    print(f"Sorry, {actor_name} you need {(1250.50 - total_points):.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
