#!/usr/bin/python3
for char in range(ord('a'), ord('z')+1):
    if char != ord('a') and char != ord('q'):
        print(chr(char), end='')

print('$', end='')