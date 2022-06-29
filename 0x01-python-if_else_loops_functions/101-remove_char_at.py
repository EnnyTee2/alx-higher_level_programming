#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for x in str:
        if x == str[n]:
            continue
        else:
            copy += x
    return copy
