#!/usr/bin/python3
""" module docstring here.. """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ return width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets the value of width """
        if isinstance(value, (int, float)) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ sets the value of height """
        if isinstance(value, (int, float)) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ sets the value of x"""
        if isinstance(value, (int, float)) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ sets the value of y """
        if isinstance(value, (int, float)) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """ displays the rectangle with '#'"""
        xw = self.__x + self.__width
        yh = self.__y + self.__height
        rec = [[' ' for _ in range(xw)]
               for _ in range(yh)]

        for i in range(yh):
            for j in range(xw):
                if i >= self.__y and j >= self.__x:
                    rec[i][j] = '#'
            if '#' in rec[i]:
                pass
            else:
                rec[i] = []

        for row in rec:
            print(''.join(row))

    def __str__(self):
        """ returns the rectangle string """
        return (
            f"[Rectangle] ({self.id}) {self.__x}"
            f"/{self.__y} - {self.width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        """ updates rectangle attributes """
        if len(args) != 0:
            keys = ["id", "width", "height", "x", "y"]
            attributes = dict(zip(keys, args))

            for key, value in attributes.items():
                if isinstance(value, int) is False:
                    raise TypeError(f"{value} must be an integer")
                if value < 0:
                    raise ValueError(f"{value} must be >= 0")
            if args[0]:
                super().__init__(args[0])
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

        else:
            for key, value in kwargs.items():
                if isinstance(value, int) is False:
                    raise TypeError(f"{value} must be an integer")
                if value < 0:
                    raise ValueError(f"{value} must be >= 0")
                if 'id' in kwargs:
                    super().__init__(kwargs['id'])
                if 'width' in kwargs:
                    self.__width = kwargs['width']
                if 'height' in kwargs:
                    self.__height = kwargs['height']
                if 'x' in kwargs:
                    self.__x = kwargs['x']
                if 'y' in kwargs:
                    self.__y = kwargs['y']

    def to_dictionary(self):
        """ returns the dictionary representation of Rectangle """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
