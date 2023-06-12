#!/usr/bin/python3
""" module docstring goes here """


Rectangle = __import__('9-rectangle').Rectangle

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
        return ("[Square] {}/{}".format(self.__size, self.__size))
