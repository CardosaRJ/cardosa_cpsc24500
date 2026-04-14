"""
order.py - Week 3 Starter

The Order class represents a customer's order containing one or more MenuItems.

Attributes:
- customer_name (str)
- items (list of MenuItem)

Methods:
- add_item(item): append a MenuItem to the order
- remove_item(index): remove an item by 1-based index
- subtotal(): sum of all item prices
- tax(): subtotal * 0.0875
- total(): subtotal + tax
- __str__: formatted receipt string
"""

from menu_item import MenuItem

TAX_RATE = 0.0875


class Order:

    def __init__(self, customer_name):
        # TODO: store the customer name
        # TODO: initialize an empty list for items
        pass

    def add_item(self, item):
        # TODO: append the item to self.items
        pass

    def remove_item(self, index):
        # TODO: remove the item at position (index - 1) since the menu shows 1-based numbers
        # Hint: use self.items.pop(index - 1)
        pass

    def subtotal(self):
        # TODO: return the sum of prices for all items
        pass

    def tax(self):
        # TODO: return self.subtotal() * TAX_RATE
        pass

    def total(self):
        # TODO: return subtotal + tax
        pass

    def __str__(self):
        # TODO: build and return a formatted receipt string
        # Include: header, customer name, each item with number, subtotal, tax, total
        pass
