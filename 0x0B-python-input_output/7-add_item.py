#!/usr/bin/python3
"""#!/usr/bin/python3

a script that adds all arguments to a
Python list, and then save them to a file:
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    class Run:
        arg_list = []

        def __init__(self):
            self.arg_list.extend(sys.argv[1:])
            filename = "add_item.json"
            save_to_json_file(self.arg_list, filename)

            self.arg_list = load_from_json_file(filename)
    a = Run()
Add all arguments to a Python list and save them to a file."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
