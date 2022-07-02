#!/usr/bin/python3

"""a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for integer in matrix[x]:
            print("{:d}".format(integer), end=" ")
        print("")
