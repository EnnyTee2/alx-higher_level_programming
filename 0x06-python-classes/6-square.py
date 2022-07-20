#!/usr/bin/python3

"""a class Square that defines a
square (based on 5-square.py) with private instance attributes
and a properties which are accessed and changed
by getters and setters respectively"""


class Square:
    """"
    Square (class): creates a square with the size specified by
    the parameter size and raise error if type is not int or
    size is less than zero.
    Attributes:
        size (int): specify the size of the square.
        position(): specifies a tuple containing square pos
        area(): returns the area of the square.
        my_print(): prints out the square with # character to stdout.
    Args:
        size (int): size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
    @property
    def position(self):
        return self.__position
 
    @position.setter
    def position(self, value):
        if (type(value) is tuple and len(value) == 2):
            if checker(value) is True
                    self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates area of the square and return the result"""

        return self.__size * self.__size

    def my_print(self):
        """ Prints the square with the character # to the stdout
        depending on the position specified"""

        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
                for i in range(self.__size):
                    print("_" * self.__position[0] + "#" * self.__size) 
            else:
                for i in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
