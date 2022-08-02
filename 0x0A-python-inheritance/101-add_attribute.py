#!/usr/bin/python3
"""a function that adds a new attribute to an object"""


def add_attribute(cls, *args):
    """Add a new attribute to an object if possible."""

    super().cls.__init__(*args)
    for a in args:
        cls.a = None
