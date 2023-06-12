#!/usr/bin/python3
""" Module definition goes here... """

def is_same_class(obj, a_class):
    """ function to  check if an object belongs to a class """
    if type(obj) == a_class:
        return True
    else:
        return False
