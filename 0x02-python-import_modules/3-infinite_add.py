#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    size = len(argv)
    add = 0
    if size > 1:
        for i in range(1, size):
            add += int(argv[i])
    print(add)
