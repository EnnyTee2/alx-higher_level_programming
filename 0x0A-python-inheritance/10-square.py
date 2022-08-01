#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self.__width = self.__size
        self.__height = self.__size
