#!/usr/bin/python3

""" a function that deletes keys with
a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    for key, values in a_dictionary.items():
        if values == value:
            a_dictionary.pop(key, None)
            continue
    return a_dictionary
