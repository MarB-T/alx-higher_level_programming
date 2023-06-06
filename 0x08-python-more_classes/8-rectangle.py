#!/usr/bin/python3
""" The rectangle Module """


class Rectangle:
    """ Definition of class Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize the class Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ returns a string of '#' rectangle """
        rectangle_repr = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for h in range(self.__height):
            [rectangle_repr.append(Rectangle.print_symbol) for j in range(self.__width)]
            if h != (self.__height - 1):
                rectangle_repr.append('\n')
        return ("".join(rectangle_repr))

    def __repr__(self):
        """ rectangle representation """
        rectangle_repr = "Rectangle(" + str(self.__width)
        rectangle_repr += ", " + str(self.__height) + ")"
        return (rectangle_repr)

    def __del__(self):
        """ delete Rectangle instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """check for equality"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area() > rect_1.area()):
            return (rect_2)
        return (rect_1)
