#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k, v in a_dictionary.items():
        if k == key:
            del a_dictionary[k]
            break
    return (a_dictionary)
