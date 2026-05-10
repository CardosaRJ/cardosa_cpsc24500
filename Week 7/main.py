"""
main.py - Week 7 Starter

Flow:
1. Ask for a path to a word file, load via WordCollection.from_file()
2. Print a count per part of speech
3. Show available story templates and let the user pick one
4. Ask how many sentences to generate
5. Generate and print the sentences
6. Ask if the user wants another story (loop if yes)
"""

from word_collection import WordCollection
from story_template import TEMPLATES


def main():
    # TODO: ask for the path; load the WordCollection
    # TODO: print summary (count per part of speech)
    # TODO: loop:
    #   - show templates with numbers
    #   - get user choice
    #   - ask how many sentences
    #   - call template.generate(words) for each
    #   - ask "Generate another story?" and break if not yes
    path = input("Enter the path to the word file: ").strip()
    words = WordCollection.from_file(path)

    print(f"\nLoaded {len(words)} words:")
    for pos in ["adj", "adv", "n", "prep", "v"]:
        count = len(words.filter_by_pos(pos))
        print(f"{pos}: {count}")

    print("\nLet's tell some stories!")

    while True:
        print("\nAvailable story styles:")
        for i, template in enumerate(TEMPLATES, 1):
            print(f"{i}. {template.name}")

        while True:
            try:
                choice = int(input("\nChoose your story style: "))
                if 1 <= choice <= len(TEMPLATES):
                    template = TEMPLATES[choice - 1]
                    break
                print("That is not a valid choice.")
            except ValueError:
                print("Please enter a number.")

        num = int(input("How many sentences will your story be? "))
        print(f"\n--- {template.name} Story ---")
        for _ in range(num):
            print(template.generate(words))
        print()

        again = input("Care to generate another story? (y/n): ").strip().lower()
        if again != "y":
            break

    print("I hope you enjoyed your time with StoryTeller!")


if __name__ == "__main__":
    main()
