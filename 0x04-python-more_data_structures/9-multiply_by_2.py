#!/usr/bin/python3

"""a function that returns a new
dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    new_dico = {}
    for key in a_dictionary.keys():
        new_dico[key] = a_dictionary[key] * 2
    return new_dico
