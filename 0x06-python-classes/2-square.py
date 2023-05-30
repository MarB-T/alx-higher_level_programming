#!/usr/bin/python3
"""
    Square module declaration

"""


class Square:
    """ Square variables and artributes """

    def __init__(self, size=0):
        """ Inittializes square
        Args:
            size
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
