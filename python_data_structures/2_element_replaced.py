#!/usr/bin/python3

def replace_element(lst, index, element):
    if 0 <= index < len(lst):
        lst[index] = element

if __name__ == "__main__":
    list_ = [5, 4, 3, 2, 1]
    index = 1
    element_to_replace = 5

    replace_element(list_, index, element_to_replace)

    print(list_)
