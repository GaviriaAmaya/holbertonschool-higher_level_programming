#!/usr/bin/python3
for i in range(9):
    for j in range(10):
            if (i == 8 and j == 9):
                print("{:d}{:d}".format(i, j))
            elif (i != j and i < j):
                print("{:d}{:d}, ".format(i, j), end="")