#!/usr/bin/python3

"""a function that adds 2 tuples.""""


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


    """a1 = tuple_a[0]
    a2 = tuple_a[1]
    b1 = 0
    b2 = 0
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_b > 1:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    else:
        try:
            b1 = tuple_b[0]
        except:
            pass
        try:
            b2 = tuple_b[1]
        except:
            pass
    return (a1 + b1, a2 + b2)""""
