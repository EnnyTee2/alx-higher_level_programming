#!/usr/bin/python3

""" a function that retrieves an element from a list like in C."""


def element_at(my_list, idx):
    if idx < 0:
        return None
    else:
        if len(my_list) - 1 > idx:
            return my_list[idx]
        else:
            return None
