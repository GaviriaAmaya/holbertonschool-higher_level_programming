#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as helloFile:
        print(helloFile.read(), end="")
