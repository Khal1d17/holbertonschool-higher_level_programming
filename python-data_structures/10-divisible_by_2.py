#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(0,len(my_list)+1):
        if i % 2 == 0:
            print(f"{i} is devisible by 2")
        else:
            print(f"{i} is not devisible by 2")
