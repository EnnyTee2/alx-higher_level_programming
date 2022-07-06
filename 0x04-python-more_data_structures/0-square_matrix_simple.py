#!/usr/bin/python3

"""a function that computes the square
value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    new_mat = [i[:] for i in matrix]
    for x in range(len(new_mat)):
        for y in range(len(new_mat[x])):
            new_mat[x][y] *= new_mat[x][y]
    return new_mat
