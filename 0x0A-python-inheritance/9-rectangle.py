#!/usr/bin/python3
""" module docstring goes here """


class BaseGeometry:
    """ class BaseGeometry definition """

    def area(self):
        """ calculates area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the vale passed to be int and > 0 """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectange class definition """
    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """returns area of rectangle"""
        return (self._width * self._height)

    def __str__(self):
        """ what print Rectangle does """
        return ("[Rectangle] {}/{}".format(self._width, self._height))
