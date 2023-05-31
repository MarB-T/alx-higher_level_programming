#!/usr/bin/python3

class MagicClass:
    """
    magic class from bytecode


    """
    pi = 3.142857143

    def __init__(self, radius):
        """ initialize """
        self.__radius = None

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return 2 * pi * self.__radius ** 2

    def circumference(self):
        return 2 * pi * self.__radius
