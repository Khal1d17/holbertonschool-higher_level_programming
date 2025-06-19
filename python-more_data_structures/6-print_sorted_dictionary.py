#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary.keys())
    a.sort()
    for i in a:
        print(f"{i}: {a_dictionary[i]}")
