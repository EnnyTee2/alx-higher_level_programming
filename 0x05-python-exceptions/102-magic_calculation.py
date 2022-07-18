#!/usr/bin/python3

"""python function to produce given bytecode"""

def magic_calculation(a, b):
    result = 0
    for i in range(103):
        try:
            if a > i:
                pass
            else:
                result = a ** b / i
                
