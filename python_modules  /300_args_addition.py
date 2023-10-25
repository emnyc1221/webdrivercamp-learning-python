#!/usr/bin/python3
import sys

if __name__ == "__main":
    arguments = sys.argv[1:]
    total = sum(map(int, arguments))

    print(total)
