#!/usr/bin/python3
""" module docstring goes here """


def write_file(filename="", text=""):
    """ function to writea string to a text file and return number of charcters written """
    f = open(filename, "w")
    c = f.write(text)
    f.close()
    return c
