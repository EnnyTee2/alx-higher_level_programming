#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """this clas has its neq and eq operators inverted"""

    def __ne__(self, value):
        """override parent __neq__ method"""
        super().__ne__(value)
        return self == value

    def __eq__(self, value):
        """override parent __eq__ method"""
        super().__eq__(value)
        return self != value
