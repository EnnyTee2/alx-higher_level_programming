#!/usr/bin/python3

"""a function that returns the weighted
average of all integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    wa_sum = 0
    div = 0
    for score, weight in my_list:
        wa_sum += (score * weight)
        div += weight 
    return wa_sum / div
