#!usr/bin/python3
""" module docstring goes here """


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using json representation """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
