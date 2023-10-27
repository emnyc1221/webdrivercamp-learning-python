#!/usr/bin/python3

def tuple_addition(first_arg=(), second_arg=()):
    first_element = first_arg[0] if len(first_arg) >= 1 else 0
    second_element = first_arg[1] if len(first_arg) >= 2 else 0
    third_element = second_arg[0] if len(second_arg) >= 1 else 0
    fourth_element = second_arg[1] if len(second_arg) >= 2 else 0

    result = (first_element + third_element, second_element + fourth_element)
    return result

if __name__ == "__main__":
    first_arg, second_arg = (1, 99), (-1, 1)
    result = tuple_addition(first_arg, second_arg)
    print(result)

    print(tuple_addition(first_arg, (1,)))
    print(tuple_addition((1, 2, 3, 4), (-1, -2, -3, -4)))
    print(tuple_addition())
