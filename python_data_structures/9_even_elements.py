#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]

def create_even_odd_tuple(input_list):
    even_odd_tuple = tuple(num % 2 == 0 for num in input_list)
    return even_odd_tuple

if __name__ == "__main__":
    even_odd_tuple = create_even_odd_tuple(my_list)

    print(my_list)
    print(even_odd_tuple)
