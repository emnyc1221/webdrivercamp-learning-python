#!/usr/bin/python3

def dict_print(dict_):
    for key in sorted(dict_.keys()):
        print(f"{key}: {dict_[key]}")

if __name__ == "__main__":
    dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)
