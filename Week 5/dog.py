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
        super().__init__(name, "Dog")
        self.breed = breed

    def feed(self):
        # TODO: dog-specific feeding
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 20)
        print(f"Wet dog food, what a treat! {self._name} is gobbling it up.")

    def play(self):
        # TODO: dog-specific play
        self.happiness = min(100, self.happiness + 50)
        self.energy = max(0, self.energy - 25)
        self.hunger = max(0, self.hunger - 15)
        print(f"Look at how fast {self._name} chases that frisbee. They are gonna be so tuckered out later!")

    def fetch(self):
        # TODO: return a fetch-themed string
        print(f"Throw a dog a bone. {self._name} fetched it so quick! Are they gonna give that back?")
