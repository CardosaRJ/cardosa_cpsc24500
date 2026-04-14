"""
main.py - Week 3 Starter

Menu-driven point-of-sale program.

Flow:
1. Welcome banner
2. Ask for customer name, create an Order
3. Show the drink menu, let the customer pick a drink and size
4. Build a MenuItem and add it to the order
5. Show: add another drink / remove a drink / view order / check out
6. On checkout, print the formatted receipt
"""

from menu_item import MenuItem
from order import Order

DRINKS = [
    ("Americano", 3.50),
    ("Cappuccino", 4.25),
    ("Espresso", 3.00),
    ("Latte", 4.75),
]

SIZES = [
    ("Small", 0.00),
    ("Medium", 0.75),
    ("Large", 1.25),
]


def show_drink_menu():
    # TODO: print the drink list with numbers and prices
    pass


def show_size_menu():
    # TODO: print the size list with numbers and upcharges
    pass


def choose_drink():
    """Prompt for a drink and size, return a new MenuItem."""
    # TODO: show drink menu, get choice (1-4)
    # TODO: show size menu, get choice (1-3)
    # TODO: compute price = base + upcharge
    # TODO: return MenuItem(name, size, price)
    pass


def main():
    # TODO: print welcome banner
    # TODO: ask for customer name and create an Order
    # TODO: add the first drink

    # TODO: loop showing the action menu (add / remove / view / check out)
    #       until the user checks out

    # TODO: on checkout, print the order (uses Order.__str__)
    pass


if __name__ == "__main__":
    main()
