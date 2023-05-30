#!usr/bin/python3
"""
    class Square declaration


"""


class Square:
    """ objects and variables of class """
    def __init__(self, size=0):
        """ Object initialization
        Args:
            size
        """
        self.__size = size

    @property
    def size(self):
        """Gets size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
