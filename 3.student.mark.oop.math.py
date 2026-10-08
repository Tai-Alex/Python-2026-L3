import math
import numpy as np
import curses

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
    def get_gpa(self, courses):
        marks = []
        credits = []
        for course in courses:
            marks.append(self.get_mark(course.get_id()))
            credits.append(course.get_credit())
        marks = np.array(marks)
        credits = np.array(credits)
        gpa = np.sum(marks * credits) / np.sum(credits)
        return gpa

class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        self.__credit = int(input("Course Credit: "))
        print("---------------------------")
    def list(self):
        print(f"Course ID: {self.__id} | Name: {self.__name} | Credit: {self.__credit}")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit

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
            course = Course("", "", "")
            course.input()
            self.courses.append(course)
        print()
    def input_marks(self):
        print("===ENTER MARKS OF THE COURSES===")
        print()
        for course in self.courses:
            print(f"Course: {course.get_name()}")
            for student in self.students:
                print(f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | Mark: ", end = "")
                mark = float(input())
                mark = math.floor(mark * 10) / 10
                student.add_mark(course.get_id(), mark)
            print()
    def list_students(self):
        print("===STUDENT LIST===")
        for student in self.students:
            print(f"ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()}")
        print()
    def list_courses(self):
        print("===COURSE LIST===\n")
        for course in self.courses:
            print(f"ID: {course.get_id()} | Name: {course.get_name()} | Credits: {course.get_credit()}")
        print()
    def show_student_marks(self):
        print("===SHOW MARKS OF THE COURSES===")
        print()
        for course in self.courses:
            print(f"Course: {course.get_name()} | Credits: {course.get_credit()}")
            for student in self.students:
                print(f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | Mark: {student.get_mark(course.get_id())}")
            print()
    def show_student_gpa(self):
        print("\n===GPA OF STUDENTS===\n")
        for student in self.students:
            print(f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | GPA: {student.get_gpa(self.courses):.2f}")
    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.get_gpa(self.courses), reverse = True)

    def show_students_curses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(2, 5, "=========STUDENTS=========")
        row = 4
        for student in self.students:
            text = (f"ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()}")
            stdscr.addstr(row, 5, text)
            row += 1
        stdscr.addstr(row + 2, 5, "Press any key to return...")
        stdscr.refresh()
        stdscr.getch()

    def show_courses_curses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(2, 5, "==========COURSES==========")
        row = 4
        for course in self.courses:
            text = (f"ID: {course.get_id()} | Name: {course.get_name()} | Credits: {course.get_credit()}")
            stdscr.addstr(row, 5, text)
            row += 1
        stdscr.addstr(row + 2, 5, "Press any key to return...")
        stdscr.refresh()
        stdscr.getch()

    def show_marks_curses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(2, 5, "========STUDENT MARKS========")
        row = 4
        for course in self.courses:
            stdscr.addstr(row, 5, f"Course: {course.get_name()} | Credits: {course.get_credit()}")
            row += 1
            for student in self.students:
                text = (f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | Mark: {student.get_mark(course.get_id())}")
                stdscr.addstr(row, 7, text)
                row += 1
            row += 1
        stdscr.addstr(row, 5, "Press any key to return...")
        stdscr.refresh()
        stdscr.getch()       

    def show_gpa_curses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(2, 5, "=========STUDENT GPA=========")
        row = 4
        for student in self.students:
            text = (f"Student ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_DoB()} | GPA: {student.get_gpa(self.courses):.2f}")
            stdscr.addstr(row, 5, text)
            row += 1
        stdscr.addstr(row + 2, 5, "Press any key to return...")
        stdscr.refresh()
        stdscr.getch()
    

def menu(stdscr, management):
    while True:
        stdscr.clear()

        stdscr.addstr(2, 5, "===========================================")
        stdscr.addstr(3, 5, "         STUDENT MANAGEMENT SYSTEM         ")
        stdscr.addstr(4, 5, "===========================================")
        stdscr.addstr(6, 5, "1. Show Students")
        stdscr.addstr(7, 5, "2. Show Courses")
        stdscr.addstr(8, 5, "3. Show Marks")
        stdscr.addstr(9, 5, "4. Show GPA")
        stdscr.addstr(10, 5, "5. Sort by GPA")
        stdscr.addstr(11, 5, "0. Exit")
        stdscr.addstr(13, 5, "Enter your choice: ")
        
        stdscr.refresh()
        choice = chr(stdscr.getch())
        if choice == "1": management.show_students_curses(stdscr)
        if choice == "2": management.show_courses_curses(stdscr)
        if choice == "3": management.show_marks_curses(stdscr)
        if choice == "4": management.show_gpa_curses(stdscr)
        if choice == "5": 
            management.sort_students_by_gpa()
            stdscr.clear()
            stdscr.addstr(5, 5, "Students sorted by GPA successfully !")
            stdscr.addstr(7, 5, "Press any key to return")
            stdscr.refresh()
            stdscr.getch()
        if choice == "0": break

def main():
    managent = StudentManagement()
    managent.input_students()
    managent.input_courses()
    managent.input_marks()

    curses.wrapper(menu, managent)

main()