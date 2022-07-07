bad_grades = int(input())
counter_bad_graded = 0
number_of_problems = 0
total_grade = 0
last_problem = ""
has_failed = True

while counter_bad_graded < bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        counter_bad_graded += 1
    total_grade += grade
    number_of_problems += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_score = total_grade / number_of_problems
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
