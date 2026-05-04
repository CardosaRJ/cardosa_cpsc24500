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
    try:
        r = float(input("Enter radius: "))
        gallery.add_shape(Circle(r))
        print("The circle has been added to your gallery!")
    except ValueError as e:
        print(f"Failed to add circle: {e}")


def add_rectangle(gallery):
    # TODO
    try:
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        gallery.add_shape(Rectangle(w, h))
        print("The rectangle has been added to your gallery!")
    except ValueError as e:
        print(f"Failed to add rectangle: {e}")


def add_triangle(gallery):
    # TODO
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        gallery.add_shape(Triangle(a, b, c))
        print("The triangle has been added to your gallery!")
    except ValueError as e:
        print(f"Failed to add triangle: {e}")


def main():
    gallery = Gallery("My Shapes")
    # TODO: loop showing the menu and dispatching to the right function

    while True:
        print("\n" + "*" * 44)
        print("        Welcome To The Shape Gallery")
        print("*" * 44)
        print("(1) Add a circle")
        print("(2) Add a rectangle")
        print("(3) Add a triangle")
        print("(4) Display all shapes")
        print("(5) Show total area")
        print("(6) Show largest shape")
        print("(7) Quit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_circle(gallery)
        elif choice == "2":
            add_rectangle(gallery)
        elif choice == "3":
            add_triangle(gallery)
        elif choice == "4":
            gallery.display_all()
        elif choice == "5":
            print(f"Total area of all your shapes: {gallery.total_area():.2f}")
        elif choice == "6":
            largest = gallery.largest_shape()
            if largest:
                print(f"The largest shape in your gallery is {largest.describe()}, sporting an area of {largest.area():.2f})")
            else:
                print("Your gallery is currently empty.")
        elif choice == "7":
            print("Have a wonderful day!")
            break
        else:
            print("Not a valid choice. Please try again.")


if __name__ == "__main__":
    main()
