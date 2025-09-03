#!/usr/bin/python3
import sys

if __name__ == "__main__":
    x = 0
    for i in range(1, len(sys.argv)):
        x += int(sys.argv[i])
    print("{}".format(x))
