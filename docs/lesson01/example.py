# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

# Import the math module so we can use math.pi and math.sqrt.
import math

# Print a description of this program.
print("This program computes and outputs the")
print("surface area of a right circular cone.")

# Get the radius and the height from the user.
radius = float(input("Enter the radius of a cone: "))
height = float(input("Enter the height of a cone: "))

# Compute the surface area of the cone.
radical = math.sqrt(radius**2 + height**2)
surf_area = math.pi * radius * (radius + radical)

# Print the surface area rounded to one digit
# after the decimal point for the user to see.
print(f"The surface area is {surf_area:.1f}")
