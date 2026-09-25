def input_number_of_students():
    while True:
        n = int(input("Enter number of students: "))

        if n > 0:
            return n

        print("Invalid number!")


def input_students(n):
    students = []

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


def input_number_of_courses():
    while True:
        n = int(input("\nEnter number of courses: "))

        if n > 0:
            return n

        print("Invalid number!")


def input_courses(n):
    courses = []

    for i in range(n):
        print(f"\n--- Course {i + 1} ---")

        course_id = input("ID: ")
        name = input("Name: ")

        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)

    return courses

def input_marks(students, courses):
    course_id = input("\nEnter course ID to input marks: ")

    # Find course
    course = None

    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found!")
        return {}

    print(f"\nEntering marks for: {course['name']}")

    marks = {}

    for student in students:
        mark = float(
            input(f"{student['id']} - {student['name']}: ")
        )

        marks[student["id"]] = mark

    return {
        "course_id": course_id,
        "marks": marks
    }

def list_courses(courses):
    print("\n========== COURSE LIST ==========")

    for course in courses:
        print(
            f"ID: {course['id']} | "
            f"Name: {course['name']}"
        )

def list_students(students):
    print("\n========== STUDENT LIST ==========")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Date of Birth: {student['dob']}"
        )

def show_marks(students, courses, marks_data):
    course_id = input("\nEnter course ID: ")

    # Find course
    course = None

    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found!")
        return

    # Check whether marks have been entered
    if not marks_data:
        print("No marks available!")
        return

    if marks_data["course_id"] != course_id:
        print("No marks available for this course!")
        return

    print("\n========== MARKS ==========")

    print(
        f"Course: {course['id']} - {course['name']}\n"
    )

    for student in students:
        student_id = student["id"]

        if student_id in marks_data["marks"]:
            mark = marks_data["marks"][student_id]

            print(
                f"ID: {student_id} | "
                f"Name: {student['name']} | "
                f"Mark: {mark:.2f}"
            )

def main():

    # 1. Input number of students
    number_of_students = input_number_of_students()

    # 2. Input student information
    students = input_students(number_of_students)

    # 3. Input number of courses
    number_of_courses = input_number_of_courses()

    # 4. Input course information
    courses = input_courses(number_of_courses)

    # 5. Input marks
    marks_data = input_marks(students, courses)

    # 6. List courses
    list_courses(courses)

    # 7. List students
    list_students(students)

    # 8. Show marks
    show_marks(students, courses, marks_data)

main()