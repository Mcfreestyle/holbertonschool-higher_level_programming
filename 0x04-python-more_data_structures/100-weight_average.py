#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    s = 0
    d = 0
    for i1, i2 in my_list:
        s += i1 * i2
        d += i2
    return (s/d)
