"""
CSE 111
Lesson 09 ICE - Dictionaries & CSV Files
Author: [Your Name]

Description:
Practice reading files using CSV reader and practice using dictionaries.

Objectives
    • Read a CSV file into a compound dictionary (dictionary of lists).
    • Use the dictionary for fast SKU look-ups.

CSV Format  (inventory.csv)
    SKU,Name,Category,Quantity
    A100,Apples,Fruit,50
    …

Program Requirements
  1. Write a `read_inventory(filename, key_col)` function that:
       • Opens a CSV file with `with open(...)`.
       • Uses `csv.reader` to read rows.
       • Skips the header row.
       • Builds and returns a dictionary where…
         - key   = value from `key_col` (use SKU column index)
         - value = entire row list.

         Example:
         {'A100': ['A100', 'Apples', 'Fruit', '50'],
          'A101': ['A101', 'Bananas', 'Fruit', '40'],
          ...
         }

  2. In `main()`:
       • Call `read_inventory("ice_09_inventory.csv", SKU_INDEX)`.
       • Prompt the user for an SKU in a loop.
           > Enter an SKU (or 'quit'): _
       • If SKU exists, print Name, Category, Quantity.
         Otherwise print “SKU not found.”
       • Exit when the user types `quit`.

  3. Use index constants for the row list if needed:
         SKU_INDEX      = 0
         NAME_INDEX     = 1
         CATEGORY_INDEX = 2
         QTY_INDEX      = 3

Stretch Goals
  • Add an option to print the full inventory table.
  • Allow the user to restock (increase quantity) for a given SKU.
"""

import csv

# index constants
SKU_INDEX      = 0
NAME_INDEX     = 1
CATEGORY_INDEX = 2
QTY_INDEX      = 3


def main():
    # Read inventory.csv into a compound dictionary.
    inventory = read_inventory("ice_09_inventory.csv", SKU_INDEX)

    while True:
        sku = input("\nEnter an SKU (or 'quit'): ").strip()
        if sku.lower() == "quit":
            break

        # TODO: Look up sku in dictionary and print details if found
        #       Otherwise print “SKU not found.”
        ...


def read_inventory(filename, key_col):
    """Read a CSV file and return a compound dictionary."""
    # TODO: your code here
    ...


if __name__ == "__main__":
    main()
