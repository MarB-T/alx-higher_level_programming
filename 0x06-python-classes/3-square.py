#!/usr/bin/python3
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
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ square instance/artribute """
        return (self.__size * self.__size)
