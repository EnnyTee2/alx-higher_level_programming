#!/usr/bin/python3

class Square(Rectangle):
    
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def __str__(self):
        super().__str__()
        return f"[Square] {self.__size}/{self.__size}"
