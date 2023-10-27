#!/usr/bin/python3

def get_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None

if __name__ == "__main":
    list_ = [5, 4, 3, 2, 1]
    index = 2

    result = get_element(list_, index)

    if result is not None:
        print(f"The element retrieved is {result}")
