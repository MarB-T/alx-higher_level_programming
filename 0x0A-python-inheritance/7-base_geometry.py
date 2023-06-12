#!/usr/bin/python3
""" module docstring goes here... """


class BaseGeometry:
    """ class BaseGeometry definition """


    def area(self):
        """ calculates area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the vale passed to be int and > 0 """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
