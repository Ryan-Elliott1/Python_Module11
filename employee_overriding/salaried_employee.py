"""
Program: salaried_employee.py
Author: Ryan Elliott
Last date modified: 07/8/2020
SalariedEmployee Class derived from Employee
"""

from employee_overriding.employee import Employee
import datetime


class SalariedEmployee(Employee):
    """SalariedEmployee class"""
    def __init__(self, lname, fname, address, pnum, startd, salary):
        super().__init__(lname, fname, address, pnum)
        self._start_date = startd
        self._salary = salary

    def display(self):
        return super().display() + " " + str(self._start_date) + " $" + str(self._salary)

    def give_raise(self, amt):
        """Change employees salary
        :param amt, new salary
        """
        self._salary = amt


# Driver
my_employee = SalariedEmployee('Elliott', 'Ryan', '123 Happy St', '515-123-4567', datetime.date.today(), 40000)
print(my_employee.display())
my_employee.give_raise(45000)
print(my_employee.display())
del my_employee
