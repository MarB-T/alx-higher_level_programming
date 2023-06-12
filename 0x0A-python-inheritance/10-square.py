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


class Square(Rectangle):
    """square object"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate the area"""
        return (self.__size * self.__size)

    def __str__(self):
        """return the print statement"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
