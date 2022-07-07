number_of_students = int(input())
top_students = 0
average_students = 0
poor_students = 0
fail_students = 0
total_grades = 0

for number in range(1, number_of_students + 1):
    grade = float(input())
    if 5 <= grade:
        top_students += 1
        total_grades += grade
    elif 4 <= grade <= 4.99:
        average_students += 1
        total_grades += grade
    elif 3 <= grade <= 3.99:
        poor_students += 1
        total_grades += grade
    elif 2 <= grade <= 2.99:
        fail_students += 1
        total_grades += grade

percent_top_students = top_students * 100 / number_of_students
percent_average_students = average_students * 100 / number_of_students
percent_poor_students = poor_students * 100 / number_of_students
percent_fail_students = fail_students * 100 / number_of_students
average_grade = total_grades / number_of_students

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_average_students:.2f}%")
print(f"Between 3.00 and 3.99: {percent_poor_students:.2f}%")
print(f"Fail: {percent_fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")
