"""
pet.py - Week 5 Starter

The Pet base class. Subclasses (Cat, Dog, Fish) will inherit from this.

Constructor: name, species
Attributes: hunger (start 50), happiness (start 50), energy (start 50)

Methods:
- feed(): modifies hunger (and maybe other stats)
- play(): modifies happiness/energy
- sleep(): modifies energy
- status(): returns a formatted string showing all attributes
- __str__: returns name and species
"""


class Pet:

    def __init__(self, name, species):
        # TODO: store name and species
        # TODO: set hunger, happiness, energy each to 50
        self._name = name
        self._species = species
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        # TODO: lower hunger (don't go below 0)
        self.hunger = max(0, self.hunger - 15)
        self.happiness = min(100, self.happiness + 5)
        print(f"{self._name} ate some food. They look so happy now!")

    def play(self):
        # TODO: raise happiness, lower energy
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        self.hunger = max(0, self.hunger - 5)
        print(f"{self._name} had fun playing, but now they are a bit more tired and hungry.")

    def sleep(self):
        # TODO: raise energy
        self.energy = min(100, self.energy + 100)
        self.hunger = min(100, self.hunger + 20)
        print(f"{self._name} got some good sleep. They feel refreshed but a good bit hungrier.")

    def status(self):
        # TODO: return a formatted string showing all three stats
        return f"{self._name} the {self._species} - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}."

    def __str__(self):
        # TODO: return f"{self._name} the {self._species}"
        return f"{self._name} the {self._species}"
