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
        self.customer_name = customer_name
        self.items = [] # list of ordered menu items

    def add_item(self, item):
        # TODO: append the item to self.items
        self.items.append(item)

    def remove_item(self, index):
        # TODO: remove the item at position (index - 1) since the menu shows 1-based numbers
        # Hint: use self.items.pop(index - 1)
        self.items.pop(index - 1)

    def subtotal(self):
        # TODO: return the sum of prices for all items
        return sum(item.price for item in self.items)

    def tax(self):
        # TODO: return self.subtotal() * TAX_RATE
        return self.subtotal() * TAX_RATE

    def total(self):
        # TODO: return subtotal + tax
        return self.subtotal() + self.tax()

    def __str__(self):
        # TODO: build and return a formatted receipt string
        # Include: header, customer name, each item with number, subtotal, tax, total
        lines = ["=" * 45]
        lines.append("               MOONBEAM COFFEE")
        lines.append("                   RECEIPT")
        lines.append("=" * 45)
        lines.append(f"Customer: {self.customer_name}")
        lines.append("-" * 45)

        for i, item in enumerate(self.items, 1):
            lines.append(f"{i}. {item}")

        lines.append("-" * 45)
        lines.append(f"Subtotal:          ${self.subtotal():.2f}")
        lines.append(f"Tax (8.75%):       ${self.tax():.2f}")
        lines.append("-" * 45)
        lines.append(f"TOTAL:             ${self.total():.2f}")
        lines.append("=" * 45)
        lines.append(f"Enjoy your coffee, {self.customer_name}!")
        lines.append("=" * 45)

        return "\n".join(lines)