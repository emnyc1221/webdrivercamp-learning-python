#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(matrix):
    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()

if __name__ == "__main__":
    print_matrix(matrix)
