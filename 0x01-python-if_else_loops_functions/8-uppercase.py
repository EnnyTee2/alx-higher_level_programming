#!/usr/bin/python3
def uppercase(str):
    if str.islower() == True:
        for char in str:
            temp = ord(char)
            if temp in range(97, 123):
                print("{}".format(chr(temp - 32)), end='')
    else:
        print(str)
