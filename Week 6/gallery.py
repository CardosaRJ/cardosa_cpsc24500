"""
gallery.py - Week 6 Starter

The Gallery class uses COMPOSITION. It HAS shapes -- it does NOT inherit from Shape.
Internally it stores a list of Shape objects.
"""


class Gallery:

    def __init__(self, name):
        # TODO: store the name
        # TODO: create an empty list for shapes
        self._name = name
        self._shapes = []

    def add_shape(self, shape):
        # TODO: append the shape to the internal list
        self._shapes.append(shape)

    def total_area(self):
        # TODO: return the sum of all shape areas (0.0 if empty)
        if not self._shapes:
            return 0.0
        return sum(shape.area() for shape in self._shapes)

    def largest_shape(self):
        # TODO: return the shape with the biggest area (None if empty)
        if not self._shapes:
            return None
        return max(self._shapes, key=lambda s: s.area())

    def display_all(self):
        # TODO: print the gallery name, the count, and each shape's
        #       description, area, and perimeter
        print(f"\n*** {self._name} Gallery ***")
        print(f"Total shapes: {len(self._shapes)}\n")
        for i, shape in enumerate(self._shapes, 1):
            print(f"{i}. {shape.describe()}")
            print(f"   Area:      {shape.area():.2f}")
            print(f"   Perimeter: {shape.perimeter():.2f}")
            print()