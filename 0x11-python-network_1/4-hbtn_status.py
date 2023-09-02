#!/usr/bin/python3
""" script to fetch url """
import requests


def fetch():
    """fetch url"""
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == '__main__':
    fetch()
