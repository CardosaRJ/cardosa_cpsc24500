"""
triangle.py - Week 6 Starter

Triangle extends Shape. Validate:
- All three sides are positive
- Triangle inequality: sum of any two sides must be greater than the third

Use Heron's formula for area:
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
"""

import math
from shape import Shape


class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        # TODO: validate all positive (raise ValueError otherwise)
        # TODO: validate triangle inequality (raise ValueError otherwise)
        # TODO: store the three sides
        pass

    def area(self):
        # TODO: use Heron's formula
        pass

    def perimeter(self):
        # TODO: a + b + c
        pass

    def describe(self):
        # TODO: return f"Triangle with sides {a}, {b}, {c}"
        pass
