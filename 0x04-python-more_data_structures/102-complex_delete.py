#!/usr/bin/python3

""" a function that deletes keys with
a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    for key in a_dictionary.keys():
        if dict[key] == value:
            a_dictionary.pop(key, None)
        else:
            continue
    return a_dictionary
