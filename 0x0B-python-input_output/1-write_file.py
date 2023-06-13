#!/usr/bin/python3
""" module docstring goes here """


def write_file(filename="", text=""):
    """ function to writea string to a text file and return number of charcters written """
    with open(filename, "w", encoding='UTF8') as f:
        c = f.write(text)
        f.close()
        return c
