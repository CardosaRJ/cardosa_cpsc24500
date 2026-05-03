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
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides need to be positive")
        # Triangle inequality
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError("Triangle inequality issue, new dimensions needed")
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def area(self):
        # TODO: use Heron's formula
        s = (self._side_a + self._side_b + self._side_c) / 2
        return math.sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))

    def perimeter(self):
        # TODO: a + b + c
        return self._side_a + self._side_b + self._side_c

    def describe(self):
        # TODO: return f"Triangle with sides {a}, {b}, {c}"
        return f"Triangle with sides {self._side_a}, {self._side_b}, {self._side_c}"