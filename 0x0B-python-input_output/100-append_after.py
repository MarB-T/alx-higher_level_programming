#!/usr/bin/python3
""" module docstring """


def append_after(filename="", search_string="", new_string=""):
    """inserts line of text to file after each line having search_string"""
    with open(filename) as f:
        lines = f.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if search_string in line:
                line += new_string
            file.write(line)
