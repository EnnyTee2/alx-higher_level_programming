#!/usr/bin/python3

"""a function that deletes the item
at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    try:
        del my_list[idx]
    except Exception:
        error = Exception
    return my_list
