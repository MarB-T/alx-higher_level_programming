#!/usr/bin/python3
""" module docstring goes here """


def add_attribute(obj, attr, value):
    """add attribute if possible
    Return: error if not possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
