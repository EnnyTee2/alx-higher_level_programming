#!/usr/bin/python3

"""Python class MagicClass that does exactly
the same as the given Python bytecode"""


import math


class MagicClass:
    """
    This class contains 3 methods:
    (1): Init constructor with an optional parameter radius
    (2): area: calculates the area
    (3): circumference: that calculates the circumference 
    """"

    def __init__(self, radius=0):
        
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self__radius
