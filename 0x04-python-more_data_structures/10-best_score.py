#!/usr/bin/python3

"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best = sorted(list(a_dictionary.values()))[-1]
    for key in a_dictionary.keys():
        if a_dictionary[key] == best:
            return key

"""try:
    best = sorted(list(a_dictionary.values()))[-1]
except Exception:
    error = Exception
    return None
return best"""
