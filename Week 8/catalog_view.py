"""
catalog_view.py - Week 8 Starter

The View handles ALL display and output formatting. It does not store data
and does not modify the catalog.

Keep this class focused on printing. Anything that creates or modifies items
belongs in main.py (the controller).
"""


class CatalogView:

    def display_items(self, items):
        # TODO: print each item on its own line (uses __str__)
        # If empty, print "No items to display."
        if not items:
            print("No items to display.")
            return
        for item in items:
            print(item)

    def display_message(self, message):
        # TODO
        print(message)

    def display_menu(self):
        # TODO: print the main menu
        print("\n" + "*"*50)
        print("          Library Catalog System")
        print("="*50)
        print("1. List all items")
        print("2. Search by title")
        print("3. Search by author")
        print("4. Check out item")
        print("5. Check in item")
        print("6. Add new item")
        print("7. View checked-out items")
        print("8. Save and quit")
        print("*"*50)

    def display_search_results(self, items, query):
        # TODO: print a header showing the query, then the items
        print(f"\nSearch results for '{query}':")
        self.display_items(items)
