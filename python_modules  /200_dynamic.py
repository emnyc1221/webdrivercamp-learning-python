#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]

    num_args = len(arguments)

    if num_args == 0:
        print(f"0 arguments.")
    else:
        print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")

        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")

    print()
