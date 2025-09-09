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
    # 1) Seed inventory with at least six items
    inventory = {
        # "SKU" : [name, aisle, qty]
        "A100": ["Apples",     1, 50],
        "B220": ["Bananas",    1, 40],
        "C315": ["Cereal",     5, 25],
        "D410": ["Detergent",  8, 15],
        "E522": ["Eggs",       2, 60],
        "F610": ["Flour",      4, 30],
    }

    # Menu loop
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
def add_item(inv: dict):
    """Add a brand-new SKU to the inventory dictionary."""
    sku = input("  New SKU: ").strip().upper()
    if sku in inv:
        print("  That SKU already exists.")
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
        print("  SKU not found.")
        return
    amount = int(input("  Amount to add: "))
    inv[sku][QTY_INDEX] += amount
    print(f"  New quantity: {inv[sku][QTY_INDEX]}")


def lookup_item(inv: dict):
    """Display information for a single SKU."""
    sku = input("  SKU to look up: ").strip().upper()
    if sku in inv:
        name, aisle, qty = inv[sku]
        print(f"  {sku}  {name}  (aisle {aisle})  qty {qty}")
    else:
        print("  SKU not found.")


def print_inventory(inv: dict):
    """Print every SKU line in neat columns."""
    print("\nSKU     Name                Aisle  Qty")
    print("-------------------------------------------")
    for sku, data in inv.items():
        name   = data[NAME_INDEX]
        aisle  = data[AISLE_INDEX]
        qty    = data[QTY_INDEX]
        print(f"{sku:<7} {name:<18} {aisle:>5} {qty:>5}")


def print_total(inv: dict):
    """Print the combined quantity of all items."""
    # Way 1: Using a list comprehension
    total = sum(data[QTY_INDEX] for data in inv.values())
    print(f"\nTotal items in store: {total}")

    # Way 2: Using a for loop
    total = 0
    for _, data in inv.items():
        total += data[QTY_INDEX]
    print(f"\nTotal items in store: {total}")

    # Way 3: Using a for loop
    total = 0
    for data in inv.values():
        total += data[QTY_INDEX]
    print(f"\nTotal items in store: {total}")


# run program
if __name__ == "__main__":
    main()
