#!/usr/bin/python3

"""a function that adds 2 tuples.""""


def add_tuple(tuple_a=(0,0), tuple_b=(0,0)):
    res1 = (tuple_a[0] + tuple_b[0])
    res2 = (tuple_a[1] + tuple_b[1])
    return (res1, res2)



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
