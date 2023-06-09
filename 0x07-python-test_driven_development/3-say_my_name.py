#!/usr/bin/python3
"""
Prints name
"""

def say_my_name(first_name, last_name=""):
    """
    funtion to print name

    Raises:
    TypeError: If either name is not of type str
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
