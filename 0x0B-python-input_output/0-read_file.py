#!/usr/bin/python3
""" module docstring here """


def read_file(filename=""):
    """ function to read a text file (UTF8) and print to stdout """
    with open(filename) as f:
        for line in f:
            print(line.strip())
