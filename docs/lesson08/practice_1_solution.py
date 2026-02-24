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
    # Seed the inventory dictionary with five items.
    inventory_dict = {
        # "SKU" : [name, aisle, qty]
        "A100": ["Apples",     1, 50],
        "B220": ["Bananas",    1, 40],
        "C315": ["Cereal",     5, 25],
        "D410": ["Detergent",  8, 15],
        "E522": ["Eggs",       2, 60]
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
            print(f"Invalid option: {choice}")


# helper functions
def add_item(inv: dict):
    """Add a new SKU to the inventory dictionary."""
    sku = input("  New SKU: ").strip().upper()
    if sku in inv:
        print(f"  SKU {sku} already exists.")
        return
    name  = input("  Item name: ").strip()
    aisle = int(input("  Aisle number: "))
    qty   = int(input("  Starting quantity: "))
    inv[sku] = [name, aisle, qty]
    print("  Item added.")


def restock_item(inv: dict):
    """Increase the quantity of an existing SKU."""
    sku = input("  SKU to restock: ").strip().upper()
    if sku not in inv:
        print(f"  SKU {sku} not found.")
        return
    amount = int(input("  Amount to add: "))
    inv[sku][QTY_INDEX] += amount
    print(f"  SKU: {inv[sku][NAME_INDEX]}  new quantity: {inv[sku][QTY_INDEX]}")


def lookup_item(inv: dict):
    """Display information for a single SKU."""
    sku = input("  SKU to look up: ").strip().upper()
    if sku in inv:
        name, aisle, qty = inv[sku]
        print(f"  {sku}  {name}  (aisle {aisle})  qty {qty}")
    else:
        print(f"  SKU {sku} not found.")


def print_all(inv: dict):
    """Print every SKU line in neat columns."""
    print("\nSKU     Name                Aisle  Qty")
    print("--------------------------------------")
    for sku, data in inv.items():
        name  = data[NAME_INDEX]
        aisle = data[AISLE_INDEX]
        qty   = data[QTY_INDEX]
        print(f"{sku:<7} {name:<18} {aisle:>5} {qty:>5}")


def print_total(inv: dict):
    """Print the combined quantity of all items."""
    # Way 1: Using a for loop
    total = 0
    for _, data in inv.items():
        total += data[QTY_INDEX]
    print(f"\nTotal items in store: {total}")

    # Way 2: Using a for loop
    total = 0
    for data in inv.values():
        total += data[QTY_INDEX]
    print(f"\nTotal items in store: {total}")

    # Way 3: Using a list comprehension
    total = sum(data[QTY_INDEX] for data in inv.values())
    print(f"\nTotal items in store: {total}")


# run program
if __name__ == "__main__":
    main()
