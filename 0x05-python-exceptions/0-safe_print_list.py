#!/usr/bin/python3

"""a function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    try:
        for index in range(0, x+1):
            print(my_list[index], end='')
    except Exception:
        error = Exception
            
