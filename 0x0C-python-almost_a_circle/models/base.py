#!/usr/bin/python3

class Base:
    """This class forms the base of all other classes for this project.
    It'll help manage the instance attribute id

    Attributes:
        __nb_objects (int): The number of instances of Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base
        Args:
            id (int): The identity of the new Base (object)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
