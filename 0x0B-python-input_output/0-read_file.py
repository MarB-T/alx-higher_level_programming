#!/usr/bin/python3
""" module docstring here """


def read_file(filename=""):
    """ function to read a text file (UTF8) and print to stdout """
    f = open(filename, "r")
    print(f.read(), end='')
    f.close()
