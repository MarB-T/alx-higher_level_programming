#!/usr/bin/python3
"""
Function that adds integers
"""


def add_integer(a, b=98):
    """
    Adds two integers and prints results

    Args:
        a: First int or float
        b: second int or float

    Raises:
        TypeError is a or b is not int or float

    Returns: Typcasted (int) sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
