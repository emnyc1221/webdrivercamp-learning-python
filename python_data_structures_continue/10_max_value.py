#!/usr/bin/python3

def max_value(d):
    if not d:
        return None
    return max(d, key=lambda k: d[k])

if __name__ == "__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")

    max_key = max_value(None)
    print(f"Max number - {max_key}")
