#!/usr/bin/python3

class BaseGeometry:
    
    def __init__(self):
        return self.area()
    def area(self):
        raise Exception("area() is not implemented")
