"""
Program: person.py
Author: Ryan Elliott
Last date modified: 07/8/2020
Person Class
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self._last_name = lname
        self._first_name = fname

    def display(self):
        return str(self._last_name) + ", " + str(self._first_name)
