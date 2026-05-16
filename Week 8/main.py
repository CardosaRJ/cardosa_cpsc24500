"""
main.py - Week 8 Starter (Controller)

This is the controller. It coordinates the Catalog (model), CatalogView (view),
and ItemFactory (creation).

Flow:
1. Load data/catalog.tsv at startup (use ItemFactory.create_item for each row)
2. Show the menu and read the user's choice
3. Dispatch to the right action; delegate display to CatalogView
4. On "Save and quit", write the catalog back to the file in the same format
5. Wrap risky operations in try/except so the program never crashes

Menu:
1. List all items
2. Search by title
3. Search by author
4. Check out item
5. Check in item
6. Add new item
7. View checked-out items
8. Save and quit
"""

import os
from catalog import Catalog
from catalog_view import CatalogView
from item_factory import ItemFactory

DATA_FILE = os.path.join("data", "catalog.tsv")


def load_catalog(catalog, filename):
    # TODO: open the file (catch FileNotFoundError -- start with empty catalog)
    # TODO: for each line, split on tab
    # TODO: parse fields and call ItemFactory.create_item(...)
    # TODO: set the checked_out flag if the last field is "true"
    # TODO: catalog.add_item(item)
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                if len(parts) < 6:
                    continue
                item_type = parts[0]
                title = parts[1]
                author = parts[2]
                year = parts[3]
                extras = parts[4:-1]
                checked_out = parts[-1].lower() == "true"
                try:
                    item = ItemFactory.create_item(item_type, title, author, year, *extras)
                    item._checked_out = checked_out   # set after creation
                    catalog.add_item(item)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Existing catalog not found. Starting with an empty catalog.")


def save_catalog(catalog, filename):
    # TODO: open in write mode
    # TODO: for each item in catalog.get_all_items(), write a tab-delimited line
    #       in the same format as the input file
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for item in catalog.get_all_items():
            item_type = item.get_item_type()
            
            if item_type == "Book":
                line = f"Book\t{item.title}\t{item.author}\t{item.year}\t{item._isbn}\t{item._page_count}\t{item.checked_out}"
            elif item_type == "DVD":
                line = f"DVD\t{item.title}\t{item.author}\t{item.year}\t{item._runtime_minutes}\t{item._rating}\t{item.checked_out}"
            elif item_type == "Magazine":
                line = f"Magazine\t{item.title}\t{item.author}\t{item.year}\t{item._issue_number}\t{item._month}\t{item.checked_out}"
            else:
                continue  # skip unknown types
                
            f.write(line + "\n")


def add_item_interactive(catalog, view):
    # TODO: ask for type, title, author, year, then the type-specific fields
    # TODO: use ItemFactory.create_item(...) and catalog.add_item(item)
    # TODO: catch ValueError and show a friendly message via the view
    view.display_message("\nAdd new item")
    item_type = input("Enter type (Book/DVD/Magazine): ").strip()
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year = input("Year: ").strip()
    if item_type.lower() == "book":
        isbn = input("ISBN: ").strip()
        pages = input("Page count: ").strip()
        extras = (isbn, pages)
    elif item_type.lower() == "dvd":
        runtime = input("Runtime (minutes): ").strip()
        rating = input("Rating: ").strip()
        extras = (runtime, rating)
    elif item_type.lower() == "magazine":
        issue = input("Issue number: ").strip()
        month = input("Month: ").strip()
        extras = (issue, month)
    else:
        view.display_message("Unknown item type.")
        return
    try:
        item = ItemFactory.create_item(item_type, title, author, year, *extras)
        catalog.add_item(item)
        view.display_message(f"Added: {item}")
    except ValueError as e:
        view.display_message(f"Error: {e}")


def main():
    catalog = Catalog()
    view = CatalogView()

    load_catalog(catalog, DATA_FILE)
    view.display_message(f"Catalog loaded.")

    # TODO: menu loop
    while True:
        view.display_menu()
        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            view.display_items(catalog.get_all_items())
        elif choice == "2":
            keyword = input("Enter title keyword: ").strip()
            results = catalog.search_by_title(keyword)
            view.display_search_results(results, keyword)
        elif choice == "3":
            keyword = input("Enter author keyword: ").strip()
            results = catalog.search_by_author(keyword)
            view.display_search_results(results, keyword)
        elif choice == "4":
            title = input("Enter title to check out: ").strip()
            for item in catalog.get_all_items():
                if item.title.lower() == title.lower():
                    try:
                        item.check_out()
                        view.display_message(f"Checked out: {item.title}")
                    except RuntimeError as e:
                        view.display_message(str(e))
                    break
            else:
                view.display_message("Item not found.")
        elif choice == "5":
            title = input("Enter title to check in: ").strip()
            for item in catalog.get_all_items():
                if item.title.lower() == title.lower():
                    try:
                        item.check_in()
                        view.display_message(f"Checked in: {item.title}")
                    except RuntimeError as e:
                        view.display_message(str(e))
                    break
            else:
                view.display_message("Item not found.")
        elif choice == "6":
            add_item_interactive(catalog, view)
        elif choice == "7":
            view.display_items(catalog.get_checked_out_items())
        elif choice == "8":
            save_catalog(catalog, DATA_FILE)
            view.display_message("Catalog saved. Goodbye!")
            break
        else:
            view.display_message("Sorry, that's not a valid choice.")


if __name__ == "__main__":
    main()
