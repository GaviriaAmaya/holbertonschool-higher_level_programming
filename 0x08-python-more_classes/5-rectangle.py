#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        rep = ""
        for i in range(self.__height):
            rep = "{}{}\n".format(rep, "#" * self.__width)
        return rep[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self)
        print("Bye rectangle...")
