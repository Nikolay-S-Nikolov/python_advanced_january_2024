def gather_credits(number_of_credits: int, *args):

    gathered_credits = 0
    enrolled_courses = []

    for course, credit in args:

        if gathered_credits >= number_of_credits:
            break

        if course in enrolled_courses:
            continue

        enrolled_courses.append(course)
        gathered_credits += credit

    if gathered_credits >= number_of_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
               f"Courses: {', '.join(sorted(enrolled_courses))}"

    credits_shortage = number_of_credits - gathered_credits
    return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."