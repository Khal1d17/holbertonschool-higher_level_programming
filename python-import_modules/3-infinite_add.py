#!/usr/bin/python3
import sys
if __name__ == "__main__":
    k = sys.argv[1:]
    cem = 0
    for i in k:
        cem = cem + int(i)
    print(cem)
