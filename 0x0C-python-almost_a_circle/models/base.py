#!/usr/bin/python3
"""Base module"""


class Base:
    """Base - Define Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ - Constructor Definition"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
