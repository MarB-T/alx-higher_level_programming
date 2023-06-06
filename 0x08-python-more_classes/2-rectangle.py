#!/usr/bin/python3
""" The rectangle Module """


class Rectangle:
    """ Definition of class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the class Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ reutrns the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets the width of the rectangle """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ sets the value for height """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
