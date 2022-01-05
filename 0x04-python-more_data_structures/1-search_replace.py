#!/usr/bin/python3
def search_replace(my_list, search, replace):
    function = lambda num: num if num != search else replace
    new_list = list(map(function, my_list))
    return (new_list)
