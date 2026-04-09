import math
import sys


def bad_spacing():
    x = 5
    y = 10
    result = x + y
    print("Result:", result)
    if result > 10:
        print("Greater")
    else:
        print("Smaller")


def long_line():
    s = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
         "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    return s


def missing_docstring():
    pass


class MyClass:
    def __init__(self, val):
        self.val = val

    def get_val(self):
        return self.val


if __name__ == "__main__":
    bad_spacing()
    print(long_line())
    obj = MyClass(42)
    print(obj.get_val())
