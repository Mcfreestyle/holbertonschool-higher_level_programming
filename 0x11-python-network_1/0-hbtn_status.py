#!/usr/bin/python3
"""Fetches a URL and print the response body
"""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html_utf8 = html.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html_utf8))
