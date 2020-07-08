"""
Program: student.py
Author: Ryan Elliott
Last date modified: 07/7/2020
Student class with Driver and imported Person class
"""
import datetime

from class_definitions.person import Person


class Student:
    """Student class using class Person, class Composition"""
    def __init__(self, major, startd, gpa, pers=''):
        self._person = pers
        self._major = major
        self._start_date = startd
        self._gpa = gpa

    def change_major(self, major):
        """Change students major
        :param major, new major
        """
        self._major = major

    def update_gpa(self, gpa):
        """Change students gpa
        :param gpa, new gpa
        """
        self._gpa = gpa

    def display(self):
        """display student"""
        return str(self._person.display()) + ", " + str(self._major) + " " + str(self._start_date) + " " + str(self._gpa)


# Driver
person1 = Person('Elliott', 'Ryan')
student1 = Student('Business', datetime.date.today(), 4.0, person1)
print(student1.display())
student1.change_major('Being Awesome!')
student1.update_gpa(3.0)
print(student1.display())
del(person1, student1)
