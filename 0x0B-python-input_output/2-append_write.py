#!/usr/bin/python3
""" module docstring goes here """


def append_write(filename="", text=""):
    """ function to append text to a file """
    with open(filename, "a+") as f:
        c = f.write(text)
        return c
