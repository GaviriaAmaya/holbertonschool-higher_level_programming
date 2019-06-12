#!/usr/bin/python3
"""Inheritation from Class Base: This imports all the Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle - class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ - Rectangle constructor: Defines a normal Rectangle
        Based on Width, Height, and position (X,Y) attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """height - Gets the height attribute"""
        return self.__height

    @property
    def width(self):
        """width - Gets the width attribute"""
        return self.__width

    @property
    def x(self):
        """x - Gets the x position attribute"""
        return self.__x

    @property
    def y(self):
        """y - Gets the y position attribute"""
        return self.__y

    @height.setter
    def height(self, value):
        """height - Sets the height private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """width - Sets the height private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """x - Sets the x positioner private instance"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y - Sets the y positioner private instance"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area - Define the Rectangle area"""
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """display - Shows the area of the rectangle with sharp symbol."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ - Str method application"""
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
               (self.id, self.__x, self.__y, self.__width,
                self.__height))

    def update(self, *args, **kwargs):
        """update - Updates, through args and kwargs method, the values of
           attributes. Are defined according the constructor order
        """
        if args is None or len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.width = kwargs[key]
                if key == "height":
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
