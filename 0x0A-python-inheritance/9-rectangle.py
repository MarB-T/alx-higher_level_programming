#!/usr/bin/python3
""" module docstring goes here """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
