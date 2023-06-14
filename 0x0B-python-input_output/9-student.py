#!/usr/bin/python3
""" module docstring """


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """ initalizer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of student class"""
        return (self.__dict__)
