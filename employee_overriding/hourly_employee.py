"""
Program: hourly_employee.py
Author: Ryan Elliott
Last date modified: 07/8/2020
HourlyEmployee Class derived from Employee
"""

from employee_overriding.employee import Employee
import datetime


class HourlyEmployee(Employee):
    """HourlyEmployee class"""
    def __init__(self, lname, fname, address, pnum, startd, hourp):
        super().__init__(lname, fname, address, pnum)
        self._start_date = startd
        self._hourly_pay = hourp

    def display(self):
        return super().display() + " " + str(self._start_date) + " $" + str(self._hourly_pay)

    def give_raise(self, amt):
        """Change employees hourly pay
        :param amt, new hourly pay
        """
        self._hourly_pay = amt


# Driver
my_employee = HourlyEmployee('Elliott', 'Ryan', '123 Happy St', '515-123-4567', datetime.date.today(), 10.00)
print(my_employee.display())
my_employee.give_raise(12.00)
print(my_employee.display())
del my_employee
