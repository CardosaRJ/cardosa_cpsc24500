"""
book.py - Week 8 Starter

Book extends LibraryItem with isbn (str) and page_count (int).
"""

from library_item import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, author, year, isbn, page_count, checked_out=False):
        # TODO: super().__init__(...)
        # TODO: store isbn and page_count
        super().__init__(title, author, year, checked_out)
        self._isbn = isbn
        self._page_count = int(page_count)

    def get_item_type(self):
        # TODO: return "Book"
        return "Book"

    def __str__(self):
        # TODO: extend the base __str__ with ISBN and page count
        base = super().__str__()
        return f"{base} | ISBN: {self._isbn} | Pages: {self._page_count}"
