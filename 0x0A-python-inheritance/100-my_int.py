#!/usr/bin/python3
""" module docstring goes here """


class MyInt(int):
    """ inheriting from int class"""

    def __eq__(self, other):
        """initialize == """
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        """intialize != """
        if int.__eq__(self, other):
            return True
        else:
            return False
