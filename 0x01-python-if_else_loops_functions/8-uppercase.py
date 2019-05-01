#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if j > 96 and j < 123:
            j = j - 32       
        print("{:s}".format(chr(j)), end="")
    print()
