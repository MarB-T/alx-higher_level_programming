#!/usr/bin/python3
""" module definition goes here """


def is_kind_of_class(obj, a_class):
    """ checks if object belongs to a class or instances of its inheritance """

    if isinstance(obj, a_class):
        return True
    return False
