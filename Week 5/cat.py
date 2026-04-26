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
        super().__init__(name, "Cat")

    def feed(self):
        # TODO: cat-specific feeding (different numbers than the base class)
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 35)
        print(f"Fish and milk. Yum! {self._name} is over the moon.")

    def play(self):
        # TODO: cat-specific play behavior
        self.happiness = min(100, self.happiness + 35)
        self.energy = max(0, self.energy - 15)
        self.hunger = max(0, self.hunger - 15)
        print(f"As the laser pointer zooms across the floor, {self._name} punces at it over and over.")

    def purr(self):
        # TODO: return a string like f"{self._name} purrs softly."
        print(f"{self._name} purrs contentedly.")
