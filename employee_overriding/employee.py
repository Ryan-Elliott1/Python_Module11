"""
Program: employee.py
Author: Ryan Elliott
Last date modified: 07/8/2020
Employee Class
"""


class Employee:
    """Employee class"""
    def __init__(self, lname, fname, address, pnum):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = pnum

    def display(self):
        return str(self._last_name) + ", " + str(self._first_name) + " " + str(self._address) + " " + str(self._phone_number)
