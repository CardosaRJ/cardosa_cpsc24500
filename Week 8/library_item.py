"""
library_item.py - Week 8 Starter

LibraryItem is the abstract base class for all catalog items.

Attributes (private with @property):
- title (str)
- author (str)
- year (int)
- checked_out (bool)

Abstract:
- get_item_type() -> str  (subclasses return "Book", "DVD", or "Magazine")

Concrete:
- check_out(): raise RuntimeError if already checked out
- check_in(): raise RuntimeError if already available
- __lt__: sort by title, case-insensitive
- __str__: includes type, title, author, year, status
"""

from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title, author, year, checked_out=False):
        # TODO: store as private attributes
        self._title = title
        self._author = author
        self._year = int(year)
        self._checked_out = checked_out

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def checked_out(self):
        return self._checked_out

    @abstractmethod
    def get_item_type(self):
        pass

    def check_out(self):
        # TODO: raise RuntimeError if already checked out
        # TODO: set self._checked_out = True
        if self._checked_out:
            raise RuntimeError(f"{self.title} is already checked out.")
        self._checked_out = True

    def check_in(self):
        # TODO: raise RuntimeError if already available
        # TODO: set self._checked_out = False
        if not self._checked_out:
            raise RuntimeError(f"{self.title} is not checked out.")
        self._checked_out = False

    def __lt__(self, other):
        # TODO: compare titles case-insensitively
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.title.lower() < other.title.lower()

    def __str__(self):
        # TODO: return formatted string with type, title, author, year, status
        # Status text: "CHECKED OUT" or "AVAILABLE"
        if self._checked_out:
            status = "CHECKED OUT" 
        else:
            status = "AVAILABLE"            
        return f"{self.get_item_type()} | {self.title} by {self.author} ({self.year}) - {status}"
