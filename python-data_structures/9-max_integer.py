#!/usr/bin/python3
def max_integer(my_list=[]):
    k = sorted(my_list, reversed=True)
    if len(my_list) == 0:
        return None 
    else:
        return k[0]
