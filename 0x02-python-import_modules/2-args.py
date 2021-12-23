#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    size = len(sys.argv)
    if size != 1:
        if size > 2:
            char = "s"
        else:
            char = ""
        print("{:d} argument{:s}:".format(size - 1, char))
        for i in range(1, size):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
