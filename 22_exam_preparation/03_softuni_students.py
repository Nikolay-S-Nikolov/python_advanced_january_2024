def softuni_students(*id_students, **id_courses):
    valid_students = []
    invalid_students = []
    for course_id, student_username in sorted(id_students, key=lambda x: x[1]):
        if course_id in id_courses:
            valid_students.append(f"*** A student with the username {student_username} has"
                                  f" successfully finished the course {id_courses[course_id]}!")
        else:
            invalid_students.append(student_username)

    result = '\n'.join(valid_students)
    if invalid_students:
        result += f"\n!!! Invalid course students: {', '.join(invalid_students)}"
    return result