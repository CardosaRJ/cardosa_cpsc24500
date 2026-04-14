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
    print("\n--- Drink Menu ---")
    for i, (name, price) in enumerate(DRINKS, 1):
        print(f"{i}. {name} ${price:.2f}")


def show_size_menu():
    # TODO: print the size list with numbers and upcharges
    print("\n--- Size ---")
    for i, (size_name, upcharge) in enumerate(SIZES, 1):
        print(f"{i}. {size_name} +${upcharge:.2f}")


def choose_drink():
    """Prompt for a drink and size, return a new MenuItem."""
    # TODO: show drink menu, get choice (1-4)
    # TODO: show size menu, get choice (1-3)
    # TODO: compute price = base + upcharge
    # TODO: return MenuItem(name, size, price)
    show_drink_menu()
    while True:
        try:
            choice = int(input("Choose a drink (1-4): "))
            if 1 <= choice <= 4:
                break
            print("Please choose 1-4.")
        except ValueError:
            print("Please enter a number.")

    show_size_menu()
    while True:
        try:
            size_choice = int(input("Choose a size (1-3): "))
            if 1 <= size_choice <= 3:
                break
            print("Please choose 1-3.")
        except ValueError:
            print("Please enter a number.")

    name, base_price = DRINKS[choice - 1]
    size_name, upcharge = SIZES[size_choice - 1]
    price = base_price + upcharge

    print(f"Added: {MenuItem}\n")
    return MenuItem(name, size_name, price)

def welcome_banner():
    # Prints a decorative welcome banner
    print("-" * 45)
    print("|           MOONBEAM COFFEE POS           |")
    print("-" * 45)
    print()

def main():
    # TODO: print welcome banner
    # TODO: ask for customer name and create an Order
    # TODO: add the first drink

    # TODO: loop showing the action menu (add / remove / view / check out)
    #       until the user checks out

    # TODO: on checkout, print the order (uses Order.__str__)
    welcome_banner()

    customer_name = input("\nEnter your name: ").strip()
    order = Order(customer_name)

    # First drink
    item = choose_drink()
    order.add_item(item)

    # Loop for adding, removing, viewing, checking out
    while True:
        print("\nWhat would you like to do?")
        print("1. Add another drink")
        print("2. Remove a drink")
        print("3. View order")
        print("4. Check out")

        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        # Add another drink
        if choice == 1:
            item = choose_drink()
            order.add_item(item)

        # Remove a drink
        elif choice == 2:
            if not order.items:
                print("Your order is empty!")
                continue
            print("\nCurrent order:")
            for i, item in enumerate(order.items, 1):
                print(f"{i}. {item}")
            try:
                idx = int(input("\nEnter item number to remove: "))
                order.remove_item(idx)
            except (ValueError, IndexError):
                print("Invalid item number.")

        # View current order
        elif choice == 3:
            print(order)

        # Complete order and check out
        elif choice == 4:
            print(order)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
