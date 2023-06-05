#!/usr/bin/python3
""" The rectangle Module """


class Rectangle:
    """ Definition of class Rectangle """

    def __init__(self, width, height):
        """ Initialize the class Rectangle """
        self.width = width
        self.height = height

    def width(self):
        """ reutrns the width of rectangle """
        return (self.width)

    def width(self, value=0):
        """ sets the width of the rectangle """
        if value < 0:
            raise ValueError("width must be >= 0")
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        self.width = value

    def height(self):
        """ returns the height of the rectangle """
        return (self.height)

    def height(self, value=0):
        """ sets the value for height """
        if value < 0:
            raise ValueError("width must be >= 0")
        if isinstance(vale, int) is False:
            raise TypeError("width must be an integer")
        self.height = value
