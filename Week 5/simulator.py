"""
simulator.py - Week 5 Starter

Menu-driven Pet Simulator. Demonstrates polymorphism: the same methods
(feed, play, sleep) work on every pet type.

Menu:
1. Adopt a pet (cat / dog / fish)
2. Feed a pet
3. Play with a pet
4. Put a pet to sleep
5. View all pets
6. Quit
"""

from cat import Cat
from dog import Dog
from fish import Fish


def adopt_pet(pets):
    # TODO: ask which type, get name, create the right object, append to pets
    pass


def select_pet(pets):
    """Show the list of pets and let the user pick one. Return the chosen pet."""
    # TODO: print numbered list of pets
    # TODO: get user choice and return that pet
    pass


def main():
    pets = []
    # TODO: loop showing the menu and dispatching to the right action
    #       remember: feed/play/sleep should work the same regardless of pet type
    pass


if __name__ == "__main__":
    main()
