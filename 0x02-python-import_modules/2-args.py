#!/usr/bin/python3

if __name__ == "__main__":
    """This program prints the number of and the list of its arguments"""
    import sys.argv as argv

    index = 1
    counter = len(argv)
    if counter == 1:
        print("{} argument:".format(counter))
        print("{index}: {}".format(argv[counter - 1]))
    elif counter == 0:
        print("{} arguments.".format(counter))
    else:
        print("{} arguments:".format(counter))
        while index <= counter:
            print("{}: {}".format(index, argv[index-1]))
            index += 1
