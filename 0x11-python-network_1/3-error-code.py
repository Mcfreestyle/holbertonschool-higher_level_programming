#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
   displays the body of the response (decoded in utf-8).
   Manage urllib.error.HTTPError exceptions and print:
   Error code: followed by the HTTP status code
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print("Error Code:", e.code)
