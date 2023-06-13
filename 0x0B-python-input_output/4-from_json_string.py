#!/usr/bin/python3
""" module docstring goes here """


import json


def from_json_string(my_str):
    """returns python object from json string """
    return (json.loads(my_str))
