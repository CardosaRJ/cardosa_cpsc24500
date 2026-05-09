"""
story_template.py - Week 7 Starter

A StoryTemplate holds a sentence pattern and can generate sentences from a WordCollection.

Pattern format: a list of strings.
- Literal words are plain strings: "The"
- Placeholders use braces: "{n}", "{v}", "{adj}", "{adv}", "{prep}"

Example:
    ["The", "{adj}", "{n}", "{v}", "{adv}"]

generate(words) walks through the pattern, replaces each placeholder with a random
word of that part of speech from the WordCollection, and returns the sentence
(capitalized, ending with a period).
"""

import random


class StoryTemplate:

    def __init__(self, name, pattern):
        # TODO: store name and pattern
        self._name = name
        self._pattern = pattern

    @property
    def name(self):
        return self._name

    @property
    def pattern(self):
        return self._pattern

    def generate(self, words):
        # TODO: walk through self._pattern
        #   - if token starts with "{" and ends with "}", extract the POS
        #     and pick a random Word of that POS from `words`
        #   - otherwise keep the token as-is
        # TODO: join with spaces, capitalize, add a period at the end
        sentence_parts = []
        for token in self._pattern:
            if token.startswith("{") and token.endswith("}"):
                pos = token[1:-1]
                matching = words.filter_by_pos(pos)
                if len(matching) > 0:
                    chosen = random.choice(list(matching))
                    sentence_parts.append(str(chosen))
                else:
                    sentence_parts.append(f"[{pos}]")
            else:
                sentence_parts.append(token)
        sentence = " ".join(sentence_parts)
        sentence = sentence.capitalize() + "."
        return sentence


# TODO: define at least 3 templates here
TEMPLATES = [
    # StoryTemplate("Adventure", ["The", "{adj}", "{n}", "{v}", "{adv}", "{prep}", "the", "{adj}", "{n}"]),
    # StoryTemplate("Mystery", [...]),
    # StoryTemplate("Simple", [...]),
    StoryTemplate("Adventure", ["The", "{adj}", "{n}", "{v}", "{adv}", "{prep}", "the", "{adj}", "{n}"]),
    StoryTemplate("Mystery", ["A", "{adj}", "{n}", "{adv}", "{v}", "while", "the", "{n}", "{v}", "{prep}", "the", "{n}"]),
    StoryTemplate("Simple", ["The", "{adj}", "{n}", "{v}", "{adv}"]),
]
