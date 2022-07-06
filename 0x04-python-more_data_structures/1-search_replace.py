#!/usr/bin/python3

"""a function that replaces all occurrences
of an element by another in a new list."""


def search_replace(my_list, search, replace):
    for index in range(len(my_list)):
        if my_list[index] == search:
            my_list[index] = replace
            break
