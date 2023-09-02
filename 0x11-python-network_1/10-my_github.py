#!/usr/bin/python3
""" get properties from email"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def properties():
    """ function """
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))


if __name__ == '__main__':
    properties()
