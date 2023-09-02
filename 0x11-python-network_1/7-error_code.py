#!/usr/bin/python3
"""send GET request to url and display body or error otherwise"""
import requests
import sys


def error_code():
    """ """
    url = sys.argv[1]

    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == '__main__':
    error_code()
