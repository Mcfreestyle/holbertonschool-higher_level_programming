#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL
   with the email as a parameter, and displays the body of
   the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    par = {'email': argv[2]}
    data = urlencode(par)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
