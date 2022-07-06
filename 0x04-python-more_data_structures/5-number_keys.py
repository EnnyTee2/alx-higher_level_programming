#!/usr/bin/python3

"""a function that returns the
number of keys in a dictionary."""


def number_keys(a_dictionary):
    keys = 0
    for key in a_dictionary.keys():
        keys += 1
    return keys
