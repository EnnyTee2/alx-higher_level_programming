#!/usr/bin/python3

def is_same_class(obj, a_class):
    if isinstance(obj, a_class) is True:
        if type(a_class) == obj:
            return True
    return False
