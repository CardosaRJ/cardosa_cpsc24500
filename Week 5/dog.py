"""
dog.py - Week 5 Starter

Dog extends Pet.
- Constructor takes an additional `breed` parameter
- Override feed() and play()
- Add a unique fetch() method
"""

from pet import Pet


class Dog(Pet):

    def __init__(self, name, breed):
        # TODO: call super().__init__(name, "Dog")
        # TODO: store breed
        pass

    def feed(self):
        # TODO: dog-specific feeding
        pass

    def play(self):
        # TODO: dog-specific play
        pass

    def fetch(self):
        # TODO: return a fetch-themed string
        pass
