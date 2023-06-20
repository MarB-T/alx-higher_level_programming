#!/usr/bin/python3
""" module docstring """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """ returns the square string """
        return (
            f"[Square] ({self.id}) {self.x}"
            f"/{self.y} - {self.__size}"
            )

    @property
    def size(self):
        """ return size """
        return (self.width)

    @size.setter
    def size(self, value):
        """ sets the value of size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates rectangle attributes """
        if len(args) != 0:
            keys = ["id", "size", "x", "y"]
            attributes = dict(zip(keys, args))

            for key, value in attributes.items():
                if isinstance(value, int) is False:
                    raise TypeError(f"{value} must be an integer")
                if value < 0:
                    raise ValueError(f"{value} must be >= 0")
            if args[0]:
                self.__init__(self.__size, self.x, self.y, args[0])
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if isinstance(value, int) is False:
                    raise TypeError(f"{value} must be an integer")
                if value < 0:
                    raise ValueError(f"{value} must be >= 0")
                if 'id' in kwargs:
                    self.__init__(self.__size, self.x, self.y, kwargs['id'])
                if 'size' in kwargs:
                    self.__size = kwargs['size']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self):
        """ returns the dictionary representation of Square """
        return {'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y}
