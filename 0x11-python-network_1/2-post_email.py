#!/usr/bin/python3

"""A python script that:
- accepts a URL and email as input file flag,
- then, sends a POST request to the passed URL
- displays the body of the response (decoded in UTF-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
