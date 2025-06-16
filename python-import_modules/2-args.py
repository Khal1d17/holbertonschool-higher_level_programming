#!/usr/bin/python3
import sys
if __name__ == "__main__":
    k = len(sys.argv)-1
    if k == 0:
        print("0 arguments.")
    elif k == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(k))
    for i in range(1, k+1):
        print("{}: {}".format(i, sys.argv[i]))
