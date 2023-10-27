#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
    result = ""

    for char in some_string:
        if char not in ('a', 'A'):
            result += char

    return result

if __name__ == "__main__":
    modified_string = remove_char(string)
    print(modified_string)
