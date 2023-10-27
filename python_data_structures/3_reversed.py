#!/usr/bin/python3

def print_integers_reversed(lst):
    for number in reversed(lst):
        print(number)

if __name__ == "__main__":
    list_ = [5, 4, 3, 2, 1]
    print_integers_reversed(list_)
