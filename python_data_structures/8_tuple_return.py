#!/usr/bin/python3

def tuple_return(arg):
    list_len = len(arg)
    first_element = arg[0] if list_len > 0 else None
    return list_len, first_element

if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5]
    result = tuple_return(list_)
    print(result)

    list_len, first_element = tuple_return(list_)
    print(f"List len = {list_len}\nFirst element = {first_element}")
