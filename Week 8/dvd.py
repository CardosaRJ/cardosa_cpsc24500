"""
dvd.py - Week 8 Starter

DVD extends LibraryItem with runtime_minutes (int) and rating (str).
"""

from library_item import LibraryItem


class DVD(LibraryItem):

    def __init__(self, title, author, year, runtime_minutes, rating, checked_out=False):
        # TODO
        super().__init__(title, author, year, checked_out)
        self._runtime_minutes = int(runtime_minutes)
        self._rating = rating

    def get_item_type(self):
        # TODO: return "DVD"
        return "DVD"

    def __str__(self):
        # TODO: extend with runtime and rating
        base = super().__str__()
        return f"{base} | Runtime: {self._runtime_minutes} min | Rating: {self._rating}"
