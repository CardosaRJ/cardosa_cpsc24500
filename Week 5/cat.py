"""
cat.py - Week 5 Starter

Cat extends Pet.
- Override feed() and play() with cat-specific behavior
- Add a unique purr() method
"""

from pet import Pet


class Cat(Pet):

    def __init__(self, name):
        # TODO: call super().__init__(name, "Cat")
        pass

    def feed(self):
        # TODO: cat-specific feeding (different numbers than the base class)
        pass

    def play(self):
        # TODO: cat-specific play behavior
        pass

    def purr(self):
        # TODO: return a string like f"{self._name} purrs softly."
        pass
