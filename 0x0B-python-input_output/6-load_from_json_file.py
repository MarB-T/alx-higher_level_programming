#!/usr/bin/python3
""" module docstring here """


def load_from_json_file(filename):
    """ creates an object from json file """
    import json
    with open(filename) as f:
        return(json.load(f))
