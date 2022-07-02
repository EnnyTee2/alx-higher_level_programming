#!/usr/bin/python3

"""a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for x in range(length):
        for number in matrix[x]:
            if number != (matrix[x][len(matrix[x]) - 1])
                print("{:d}".format(integer), end=" ")
            else:
                print("{:d}".format(integer))
        print("".format())
