"""
main.py - Week 6 Starter

Menu-driven Shape Gallery program.

Menu:
1. Add a circle
2. Add a rectangle
3. Add a triangle
4. Display all shapes
5. Show total area
6. Show largest shape
7. Quit

Wrap input/creation in try/except so the program never crashes on bad input.
"""

from gallery import Gallery
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle


def add_circle(gallery):
    # TODO: prompt for radius, create a Circle, add to gallery
    # Catch ValueError and print a friendly message
    pass


def add_rectangle(gallery):
    # TODO
    pass


def add_triangle(gallery):
    # TODO
    pass


def main():
    gallery = Gallery("My Shapes")
    # TODO: loop showing the menu and dispatching to the right function
    pass


if __name__ == "__main__":
    main()
