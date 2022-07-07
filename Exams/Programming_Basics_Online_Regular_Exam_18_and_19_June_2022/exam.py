students_count = int(input())
top_students_count = 0
good_students_count = 0
poor_students_count = 0
fail_students_count = 0
total_grade = 0

for student in range(students_count):
    grade = float(input())
    total_grade += grade
    if 5 <= grade:
        top_students_count += 1
    elif 4 <= grade <= 4.99:
        good_students_count += 1
    elif 3 <= grade <= 3.99:
        poor_students_count += 1
    else:
        fail_students_count += 1

average_grade = total_grade / students_count
top_students_percent = top_students_count / students_count * 100
good_students_percent = good_students_count / students_count * 100
poor_students_percent = poor_students_count / students_count * 100
fail_students_percent = fail_students_count / students_count * 100

print(f"""Top students: {top_students_percent:.2f}%
Between 4.00 and 4.99: {good_students_percent:.2f}%
Between 3.00 and 3.99: {poor_students_percent:.2f}%
Fail: {fail_students_percent:.2f}%
Average: {average_grade:.2f}
""")
