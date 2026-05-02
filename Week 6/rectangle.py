"""
rectangle.py - Week 6 Starter

Rectangle extends Shape. Validate that width and height are both positive.
"""

from shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        # TODO: validate both positive (raise ValueError otherwise)
        # TODO: store width and height
        pass

    def area(self):
        # TODO: width * height
        pass

    def perimeter(self):
        # TODO: 2 * (width + height)
        pass

    def describe(self):
        # TODO: return f"Rectangle {self._width} x {self._height}"
        pass
