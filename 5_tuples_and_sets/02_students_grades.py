number_of_students = int(input())

student_record = {}

for _ in range(number_of_students):
    name, grade_str = input().split()
    grade = float(grade_str)
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(grade)

for student_name, grades in student_record.items():
    average_grade = sum(grades) / len(grades)
    grades_string = f"{' '.join(f'{g:.2f}' for g in grades)}"
    print(f"{student_name} -> {grades_string} (avg: {average_grade:.2f})")
