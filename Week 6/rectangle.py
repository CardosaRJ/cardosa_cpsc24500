"""
rectangle.py - Week 6 Starter

Rectangle extends Shape. Validate that width and height are both positive.
"""

from shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        # TODO: validate both positive (raise ValueError otherwise)
        # TODO: store width and height
        if width <= 0 or height <= 0:
            raise ValueError("Need to have positive width and height")
        self._width = width
        self._height = height

    def area(self):
        # TODO: width * height
        return self._width * self._height

    def perimeter(self):
        # TODO: 2 * (width + height)
        return 2 * (self._width + self._height)

    def describe(self):
        # TODO: return f"Rectangle {self._width} x {self._height}"
        return f"Rectangle {self._width} x {self._height}"
