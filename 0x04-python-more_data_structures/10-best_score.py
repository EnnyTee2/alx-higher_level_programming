#!/usr/bin/python3

"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    best_ = None
    if a_dictionary is None or len(a_dictionary) == 0:
        return best_
    best = sorted(list(a_dictionary.values()))[-1]
    for key in a_dictionary.keys():
        if a_dictionary[key] == best:
            best_ = key
            break
    return best_


"""try:
    best = sorted(list(a_dictionary.values()))[-1]
except Exception:
    error = Exception
    return None
return best"""
