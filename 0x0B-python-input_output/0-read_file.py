#!/usr/bin/python3

"""a function that reads a text file (UTF8)
and prints it to stdout:"""


def read_file(filename=""):
    """reads the specified file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as myfile:
        data_read = myfile.read()
    print(data_read, end="")
