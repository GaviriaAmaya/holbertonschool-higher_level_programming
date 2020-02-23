#!/usr/bin/python3
"Function that prints strings in uppercase"


def uppercase(str):
    for i in str[:]:
        j = ord(i)
        if j in range(97, 123):
            j = j - 32
        print("{:s}".format(chr(j)), end="")
    print("")
