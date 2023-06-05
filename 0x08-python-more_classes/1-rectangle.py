#!/usr/bin/python3
""" The rectangle Module """



def check_value(value):
    """ function to check value """
    if value < 0:
        raise ValueError("width must be >= 0")
    if isinstance(value, int) is False:
        raise TypeError("width must be an integer")
    return (True)



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
        """ sets the width of the rectangle
        if value < 0:
            raise ValueError("width must be >= 0")
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        """
        if check_value(value) is True:
            self.__width = value

    @property
    def height(self):
        """ returns the height of the rectangle """
        return (self.height)

    @height.setter
    def height(self, value):
        """ sets the value for height
        if value < 0:
            raise ValueError("width must be >= 0")
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        """
        if check_value(value) is True:
            self.__height = value
