#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ''
    cont = []
    for letter in text:
        temp += letter
        if letter == '?' or letter == ':' or letter == '.':
            cont.append(temp)
            temp = ''
    cont.append(temp)
    final = [tex.lstrip() for tex in cont]
    last = final[-1:]
    for each in final:
        if each == last[0]:
            print(each, end='')
        else:
            print(each, end='\n\n')
