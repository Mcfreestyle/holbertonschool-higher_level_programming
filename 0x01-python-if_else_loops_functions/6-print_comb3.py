#!/usr/bin/python3
for i in range(100):
    digit1 = int(i / 10)
    digit2 = i % 10
    if digit1 == digit2:
        continue
    for x in range(i):
        digit1x = int(x / 10)
        digit2x = x % 10
        if (digit1x == digit2) and (digit2x == digit1):
            break
    else:
        if i != 89:
            print("{:02d}".format(i), end=", ")
        else:
            print("{:02d}".format(i))
