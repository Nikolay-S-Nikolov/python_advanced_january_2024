def students_credits(*args):
    course_and_credits_dict = {}
    result = ''

    for data in args:
        course_name, credits, max_test_points, diyan_points = data.split('-')
        course_and_credits_dict[course_name] = (int(credits) / int(max_test_points)) * int(diyan_points)

    total_credits = sum(course_and_credits_dict.values())

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits."

    else:
        credits_needed = 240 - total_credits
        result += f"Diyan needs {credits_needed:.1f} credits more for a diploma."

    for name_of_the_course, course_credit in sorted(course_and_credits_dict.items(), key=lambda x: -x[1]):
        result += f"\n{name_of_the_course} - {course_credit:.1f}"

    return result