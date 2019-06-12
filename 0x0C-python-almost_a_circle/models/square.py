#!/usr/bin/python3
"""Inheritance from Rectangle type"""
from models.rectangle import Rectangle


class Square(Rectangle)
"""Square - Defines an Square object."""


def __init__(self, size, x=0, y=0, id=None):
    """__init__ - Constructor method"""
    super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size - Gets the size
        """
        return super().width

    @size.setter
    def size(self, value):
        """size - Sets the size of a rectangle,
           according to the rectangle class
        """
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ - Str method to the Square class representation
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.height)
