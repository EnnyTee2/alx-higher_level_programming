#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """this clas has its neq and eq operators inverted"""

    def __ne__(self, other):
        """override parent __neq__ method"""
        super().__ne__(other)
        return int(self) == other

    def __eq__(self, other):
        """override parent __eq__ method"""
        super().__eq__(other)
        return int(self) != other
