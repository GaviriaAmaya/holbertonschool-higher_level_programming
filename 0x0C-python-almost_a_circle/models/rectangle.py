#!/usr/bin/python3
"Inheritation from Class Base"
from models.base import Base


class Rectangle(Base):
    "Rectangle class definition"

    def __init__(self, width, height, x=0, y=0, id=None):
        "Rectangle constructor"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        "Shows the area of the rectangle with sharp symbol."
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
               (self.id, self.__x, self.__y, self.__width,
                self.__height))
