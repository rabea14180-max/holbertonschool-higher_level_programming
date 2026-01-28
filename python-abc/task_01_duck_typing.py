#!/usr/bin/env python3
"""
Defines Shape abstract class and concrete classes Circle and Rectangle,
with a duck-typed function to print shape information.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape"""

    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object.
    Uses duck typing: assumes the object has area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
