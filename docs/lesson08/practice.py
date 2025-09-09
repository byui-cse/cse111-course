"""
CSE 111
Lesson 08 ICE - Dictionaries & Compound Values
Author: [Your Name]

Description:
Practice using a compound dictionary to track a store's inventory.

Instructions:
Complete the following program to help a small grocery store track
inventory items by SKU code.

For each SKU, store the item name, aisle, and quantity. Store the
inventory in a dictionary where the key is the SKU number and the value
is a list containing the [item name, aisle, quantity].

Menu options allow a clerk to add new items, restock, look up a single
item, print the full inventory, and show the total quantity of all items
combined.
"""

# index constants
NAME_INDEX  = 0
AISLE_INDEX = 1
QTY_INDEX   = 2

def main():
    # 1) Seed inventory with at least five items
    inventory = {
        # "SKU": [name, aisle, qty]
        "A100": ["Apples", 1, 50],
        # TODO: add 5 more...
    }

    # Menu
    while True:
        print("\n1 Add  2 Restock  3 Lookup  4 Print all  5 Total qty  6 Quit")
        choice = input("Select: ").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            restock_item(inventory)
        elif choice == "3":
            lookup_item(inventory)
        elif choice == "4":
            print_inventory(inventory)
        elif choice == "5":
            print_total(inventory)
        elif choice == "6":
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
    # TODO: ask for SKU; display info about the item or “not found”
    ...

def print_inventory(inv):
    # TODO: iterate by using for sku, data in inv.items():
    #       print nicely formatted line showing each item in the inventory
    ...

def print_total(inv):
    # TODO: sum the QTY_INDEX of every inner list and print the sum
    ...

# run program
if __name__ == "__main__":
    main()
