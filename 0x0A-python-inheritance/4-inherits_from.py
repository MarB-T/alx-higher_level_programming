#!/usr/bin/python3
""" module definition goes here"""


def inherits_from(obj, a_class):
    """ return True if the object is an instance of a class that inherited\
            (directly or indirectly) from the specified class"""
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return False
        return True
    return False
