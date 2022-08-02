#!/usr/bin/python3

"""a script that adds all arguments to a
Python list, and then save them to a file:"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """returns the object from its json representation of the string"""
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)

def load_from_json_file(filename):
    """loads the object from its json representation of the string"""
    with open(filename) as myfile:
        return json.load(myfile)

arglist = sys.argv[1:]

filename = "add_item.json"
save_to_json_file(arglist, filename)

my_list = load_from_json_file(filename)
print(my_list)
