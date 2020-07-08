"""
Program: student.py
Author: Ryan Elliott
Last date modified: 07/8/2020
Student Class derived from Person
"""

from derived_class_definitions.person import Person


class Student(Person):
    """Student class"""
    def __init__(self, studentid, lname, fname, major='Computer Science', gpa=0.0):
        super().__init__(lname, fname)
        self._student_id = studentid
        self._major = major
        self._gpa = gpa

    def display(self):
        return super().display() + ":" + "(" + str(self._student_id) + ")" + " " + str(self._major) + " " + str(self._gpa)


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
