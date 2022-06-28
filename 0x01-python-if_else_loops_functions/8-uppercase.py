#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char.islower():
            temp = ord(char)
            print("{} ".format(chr(temp - 32)), end='')
        else:
            print(char, end=' ')
