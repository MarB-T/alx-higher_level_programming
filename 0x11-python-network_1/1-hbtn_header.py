#!/usr/bin/python3
"""
Script to send a request and display the value of 'X-Request-Id' in the header
"""
import urllib.request
import sys


def resp_header():
    """ functiont to display value of one header response """
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == '__main__':
    resp_header()
