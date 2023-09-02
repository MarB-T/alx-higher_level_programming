#!/usr/bin/python3
"""Script to fetch url and display request id"""
import requests
import sys


def fetch_id():
    """function to fetch url and display id"""
    url = sys.argv[1]
    r = requests.get(url)

    print(r.headers.get("X-Request-Id"))


if __name__ == '__main__':
    fetch_id()
