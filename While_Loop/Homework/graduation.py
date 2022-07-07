student_name = input()
is_ejected = False
student_class = 1
total_grade = 0
bad_tries = 0

while student_class < 13:
    year_grade = float(input())
    if year_grade >= 4:
        total_grade += year_grade
        student_class += 1
    else:
        bad_tries += 1
        if bad_tries == 2:
            is_ejected = True
            break

if is_ejected:
    print(f"{student_name} has been excluded at {student_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
