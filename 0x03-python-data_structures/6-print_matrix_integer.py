#!/usr/bin/python3

"""a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for x in range(length):
        for integer in matrix[x]:
            print("{:d}".format(integer), end=" ")
        if x != length-1:
            print("")
