#!/usr/bin/python3

"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    return sorted(list(a_dictionary.values()))[-1]
