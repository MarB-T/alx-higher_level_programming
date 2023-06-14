#!/usr/bin/python3
""" module docstring """


Student = __import__('10-student').Student


class Student(Student):
    """ classs student based of 10-student.py """
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
