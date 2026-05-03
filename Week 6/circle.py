"""
circle.py - Week 6 Starter

Circle extends Shape. Validate that radius is positive (raise ValueError otherwise).
"""

import math
from shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        # TODO: raise ValueError if radius is not positive
        # TODO: store radius
        if radius <= 0:
            raise ValueError("Negative value given for radius")
        self._radius = radius

    def area(self):
        # TODO: return pi * r^2 (use math.pi)
        return math.pi * self._radius ** 2

    def perimeter(self):
        # TODO: return 2 * pi * r
        return 2 * math.pi * self._radius

    def describe(self):
        # TODO: return f"Circle with radius {self._radius}"
        return f"Circle with radius {self._radius}"   
