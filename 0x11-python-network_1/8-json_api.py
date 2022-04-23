#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
   with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        let = argv[1]
    else:
        let = ""

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': let})
        user = r.json()
        if len(user) > 0:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
