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
        pass

    def feed(self):
        # TODO: lower hunger (don't go below 0)
        pass

    def play(self):
        # TODO: raise happiness, lower energy
        pass

    def sleep(self):
        # TODO: raise energy
        pass

    def status(self):
        # TODO: return a formatted string showing all three stats
        pass

    def __str__(self):
        # TODO: return f"{self._name} the {self._species}"
        pass
