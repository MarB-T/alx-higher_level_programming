#!/usr/bin/python3
""" get properties from email"""
import requests
import sys


def properties():
    """ function """
    headers = {}
    headers['Authorization'] = '{} {}'.format(sys.argv[0], sys.argv[1])
    r = requests.get('https://api.github.com/users/{}'
                     .format(sys.argv[1]), headers=headers)
    print(r.json().get('id'))


if __name__ == '__main__':
    properties()
