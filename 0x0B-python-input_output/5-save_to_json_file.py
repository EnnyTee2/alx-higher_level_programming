#!/usr/bin/python3

"""a function that writes an Object to
a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """returns the object from its json representation of the string"""
    js_file = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as myfile:
        js_data = myfile.write(js_file)
    
