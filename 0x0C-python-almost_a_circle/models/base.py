#!/usr/bin/python3

class Base:
    """This class forms the base of all other classes for this project.
    It'll help manage the instance attribute id"""


    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects
