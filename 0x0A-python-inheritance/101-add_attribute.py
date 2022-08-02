#!/usr/bin/python3

def add_attribute(cls, *args):
    super().cls.__init__(*args)
    for a in args:
        cls.a = None
