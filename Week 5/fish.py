"""
fish.py - Week 5 Starter

Fish extends Pet.
- Override feed() and play()
- Also override sleep() (fish don't sleep the same way)
"""

from pet import Pet


class Fish(Pet):

    def __init__(self, name):
        # TODO: call super().__init__(name, "Fish")
        super().__init__(name, "Fish")

    def feed(self):
        # TODO: fish-specific feeding
        self.hunger = max(0, self.hunger - 60)
        self.happiness = min(100, self.happiness + 35)
        print(f"Oh, you may have poured a bit too much fishfood. But {self._name} sure looks happy about it. Hopefully they don't overeat.")

    def play(self):
        # TODO: fish-specific play
        self.happiness = min(100, self.happiness + 15)
        self.energy = max(0, self.energy - 5)
        self.hunger = max(0, self.hunger - 5)
        print(f"{self._name} is having so much fun following your finger around the glass.")

    def sleep(self):
        # TODO: fish-specific sleep behavior (different from base class)
        self.energy = min(100, self.energy + 50)
        self.hunger = min(100, self.hunger + 10)
        print(f"Looks like {self._name} has floated to the bottom of the tank. Guess it's time for a little rest.")
