#!/usr/bin/python3
""" module docstring """


Student = __import__('9-student').Student

class Student(Student):
    """ student class based of similar class """
    def to_json(self, attrs=None):
        """returns dictionary representation of instance"""
        if attrs is None:
            return (self.__dict__)
        if not isinstance(attrs, list):
            return (self.__dict__)
        if not (isinstance(attrs[elem], str) for elem in attrs):
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
