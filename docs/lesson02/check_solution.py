"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python program
named boxes.py that asks the user for two integers:  1) the number of
manufactured items and 2) the number of items that the user will pack
per box. Your program must compute and print the number of boxes
necessary to hold the items. This must be a whole number. Note that the
last box may be packed with fewer items than the other boxes.
"""

# Import the math module so that it can be used in this program.
import math

num_items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

# Compute the number of boxes.
num_boxes = math.ceil(num_items / items_per_box)

# Display the results for the user to see.
print(f"For {num_items} items, packing {items_per_box}"
f" items in each box, you will need {num_boxes} boxes.")
