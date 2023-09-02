#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys


def email_post():
    """ script to post and email to given url """
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    request = urllib.request.Reques(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    email_post()
