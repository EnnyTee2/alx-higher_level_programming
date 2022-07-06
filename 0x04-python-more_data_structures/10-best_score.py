#!/usr/bin/python3

"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
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

"""def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)"""
