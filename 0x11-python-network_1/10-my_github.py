#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
   uses the GitHub API to display your id
"""
import requests
from sys import argv
from pprint import pprint

if __name__ == '__main__':
    _, user, passwd = argv
    r = requests.get('https://api.github.com/user', auth=(user, passwd))
    my_id = r.json().get('id', None)
    print(my_id)
