#!/usr/bin/python3

def mult_values(d):
    return {key: value * 2 for key, value in d.items()}

if __name__ == "__main__":
    # Assuming you've fixed the module import issue, otherwise use an alternate import method
    dict_print = __import__('6_dict_print').dict_print

    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    new_dict = mult_values(dict_)
    dict_print(new_dict)
