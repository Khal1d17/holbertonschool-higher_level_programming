#!/usr/bin/python3
def raise_exception():
    try:
        return raise_exception()
    except TypeError:
        return ("Exception raised")
