"""
shape.py - Week 6 Starter

Shape is an ABSTRACT base class. It cannot be instantiated directly.
Concrete subclasses (Circle, Rectangle, Triangle) must implement all abstract methods.

Abstract methods:
- area() -> float
- perimeter() -> float
- describe() -> str
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        # TODO: subclasses implement this; nothing to do here
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def describe(self):
        pass
