jury_count = int(input())
all_presentation_average_grade = 0
all_presentation_total_grade = 0

presentation_name = input()
grades_count = 0

while presentation_name != "Finish":

    presentation_total_grade = 0

    for grades in range(jury_count):
        grade = float(input())
        grades_count += 1
        presentation_total_grade += grade
        all_presentation_total_grade += grade

    presentation_average_grade = presentation_total_grade / jury_count
    print(f"{presentation_name} - {presentation_average_grade:.2f}.")

    presentation_name = input()

all_presentation_average_grade = all_presentation_total_grade / grades_count
print(f"Student's final assessment is {all_presentation_average_grade:.2f}.")
