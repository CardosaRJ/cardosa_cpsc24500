"""
word_collection.py - Week 7 Starter

Holds a list of Word objects and supports iteration, indexing, filtering, and sorting.

Operator overloading:
- __len__, __getitem__, __contains__, __iter__, __repr__

Methods:
- add(word): TypeError if not a Word
- filter_by_pos(pos): returns a NEW WordCollection
- sorted_words(reverse=False): returns a NEW WordCollection sorted via Word.__lt__
- from_file(filepath): @classmethod that reads "word pos" lines and returns a WordCollection
"""

from word import Word


class WordCollection:

    def __init__(self):
        # TODO: empty internal list
        self._words = []

    @classmethod
    def from_file(cls, filepath):
        # TODO: create a new WordCollection
        # TODO: open the file, read each line
        #   - strip; skip blank lines
        #   - split into text and pos; skip lines that don't parse
        #   - create a Word and add it (catch ValueError for invalid POS)
        # TODO: return the collection
        collection = cls()
        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) != 2:
                        continue
                    try:
                        word = Word(parts[0], parts[1])
                        collection.add(word)
                    except ValueError:
                        continue
        except FileNotFoundError:
            print(f"Error: Cannot locate file {filepath}")
        return collection

    def add(self, word):
        # TODO: raise TypeError if not a Word
        # TODO: append to internal list
        if not isinstance(word, Word):
            raise TypeError("Words can only be added if they are in the Word Collection")
        self._words.append(word)

    def filter_by_pos(self, part_of_speech):
        # TODO: build a new WordCollection containing only matching words
        filtered = WordCollection()
        for w in self._words:
            if w.part_of_speech == part_of_speech:
                filtered.add(w)
        return filtered

    def sorted_words(self, reverse=False):
        # TODO: build a new WordCollection from sorted(self._words, reverse=reverse)
        # No `key` parameter -- relies on Word.__lt__
        sorted_collection = WordCollection()
        for w in sorted(self._words, reverse=reverse):
            sorted_collection.add(w)
        return sorted_collection

    def __len__(self):
        # TODO
        return len(self._words)

    def __getitem__(self, index):
        # TODO
        return self._words[index]

    def __contains__(self, item):
        # TODO
        return item in self._words

    def __iter__(self):
        # TODO: return iter(self._words)
        return iter(self._words)

    def __repr__(self):
        # TODO: return f"WordCollection({len(self)} words)"
        return f"WordCollection({len(self)} words)"
