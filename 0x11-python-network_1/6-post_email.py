#!/usr/bin/python3
"""Send POST request with email parameter"""
import requests
import sys


def post_email():
    """function to POST with email"""

    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == '__main__':
    post_email()
