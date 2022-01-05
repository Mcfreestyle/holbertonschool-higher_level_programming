#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda n: n if n != search else replace, my_list))
    return (new_list)
