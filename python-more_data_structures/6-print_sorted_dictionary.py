#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary.keys())
    a.sort()
    for i in a:
        return i ":" a_dictionary[i]
