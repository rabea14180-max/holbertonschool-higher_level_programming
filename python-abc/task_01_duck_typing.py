# task_01_duck_typing.py
from abc import ABC, abstractmethod
import math

# -----------------------------
# Abstract base class Shape
# -----------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass

# -----------------------------
# Circle class
# -----------------------------
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# -----------------------------
# Rectangle class
# -----------------------------
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# -----------------------------
# Duck typing function
# -----------------------------
def shape_info(shape):
    """
    Accept any object that has area() and perimeter() methods
    and print its area and perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    