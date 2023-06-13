#!/usr/bin/python3
""" module docstring here """


def read_file(filename=""):
    """ function to read a text file (UTF8) and print to stdout """
    with open(filename, encoding='UTF8') as f:
            print(f.read(), end='')
