class Student:
    def __init__(self, id, name, DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__marks = {}
    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student Name: ")
        self.__DoB = input("Date of Birth: ")
        print("----------------------------")
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | Date of Birth: {self.__DoB}")
    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark
    def get_mark(self, course_id):
        return self.__marks[course_id]
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_DoB(self):
        return self.__DoB
    def has_mark(self, course_id):
        return course_id in self.__marks

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        print("---------------------------")
    def list(self):
        print(f"Course ID: {self.__id} | Name: {self.__name}")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
    def input_students(self):
        n = int(input("Enter the number of students: "))
        print()
        for i in range(n):
            student = Student("", "", "")
            student.input()
            self.students.append(student)
        print()
    def input_courses(self):
        n = int(input("Enter the number of courses: "))
        print()
        for i in range(n):
            course = Course("", "")
            course.input()
            self.courses.append(course)
        print()
    def input_marks(self):
        print("===ENTER MARKS OF THE COURSES===")
        for course in self.courses:
            print(f"Course: {course.get_name()}")
            for student in self.students:
                print(f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | Mark: ", end = "")
                mark = int(input())
                student.add_mark(course.get_id(), mark)
            print()
    def list_students(self):
        print("===STUDENTS===")
        for student in self.students:
            print(f"ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()}")
        print()
    def list_courses(self):
        print("===COURSES===")
        for course in self.courses:
            print(f"ID: {course.get_id()} | Name: {course.get_name()}")
        print()
    def show_student_marks(self):
        print("===SHOW MARKS OF THE COURSES===")
        print()
        for course in self.courses:
            print(f"Course: {course.get_name()}")
            for student in self.students:
                print(f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | Mark: {student.get_mark(course.get_id())}")
            print()

def main():
    managent = StudentManagement()
    managent.input_students()
    managent.input_courses()
    managent.input_marks()
    print("\n====================================\n")
    managent.list_students()
    managent.list_courses()
    managent.show_student_marks()

main()