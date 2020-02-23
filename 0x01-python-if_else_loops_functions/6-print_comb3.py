#!/usr/bin/python3
"Print all possible combinations of two digits"
for i in range(0, 9):
    for j in range(1, 10):
        if i == j or j < i:
            continue
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j), end="")
        else:
            print("{:d}{:d}, ".format(i, j), end="")