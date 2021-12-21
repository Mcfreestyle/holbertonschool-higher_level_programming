#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and number % 10 != 0:
    ldigit = number % 10 - 10
else:
    ldigit = number % 10

if ldigit > 5:
    line = "and is greater than 5"
elif ldigit == 0:
    line = "and is 0"
else:
    line = "and is less than 6 and not 0"
print("Last digit of {} is {} {:s}".format(number, ldigit, line))
