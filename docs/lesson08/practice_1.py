"""
CSE 111
Lesson 8 - Dictionaries & Compound Values
Author: [Your Name]

Description:
Practice using a compound dictionary to track a store's inventory.

Instructions:
Complete the following program to help a small grocery store track
inventory items by SKU code.

For each SKU, store the item name, aisle, and quantity. Store the
inventory in a dictionary where the key is the SKU number and the value
is a list containing the [item_name, aisle, quantity].

Menu options allow a clerk to add new items, restock, look up a single
item, print the full inventory, and show the total quantity of all items
combined.
"""

# index constants
NAME_INDEX  = 0
AISLE_INDEX = 1
QTY_INDEX   = 2


def main():
    # Seed the inventory dictionary with five items.
    inventory_dict = {
        # "SKU": [name, aisle, qty]
        "A100": ["Apples", 1, 50],
        # TODO: add 4 more...
    }

    # Menu loop
    while True:
        print("\n[A]dd  [R]estock  [L]ookup  [P]rint all  [T]otal qty  [Q]uit")
        choice = input("Select: ").strip().upper()[0]
        if choice == "A":
            add_item(inventory_dict)
        elif choice == "R":
            restock_item(inventory_dict)
        elif choice == "L":
            lookup_item(inventory_dict)
        elif choice == "P":
            print_all(inventory_dict)
        elif choice == "T":
            print_total(inventory_dict)
        elif choice == "Q":
            break
        else:
            print("Invalid option")


# helper functions
def add_item(inv):
    # TODO: ask for SKU, name, aisle, quantity and
    #       add to dictionary only if SKU not present
    ...


def restock_item(inv):
    # TODO: ask for SKU and amount; increase quantity if found
    ...


def lookup_item(inv):
    # TODO: ask for SKU; display info about the item or "not found"
    ...


def print_all(inv):
    # TODO: iterate through all items in the inventory:
    #       print nicely formatted line for each item
    ...


def print_total(inv):
    # TODO: sum the quantity of every item and print the sum
    ...


# Run program
if __name__ == "__main__":
    main()
