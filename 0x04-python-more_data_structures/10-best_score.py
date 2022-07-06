#!/usr/bin/python3

"""a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    try:
        best = sorted(list(a_dictionary.values()))[-1]
    except Exception:
        error = Exception
        return None
    return best
