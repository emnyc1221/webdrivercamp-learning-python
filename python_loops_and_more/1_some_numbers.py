#!/usr/bin/python3
numbers_str = ""
for i in range(100):
    if i < 99:
        numbers_str += f"{i}, "
    else:
        numbers_str += str(i)
print(numbers_str)