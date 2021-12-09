# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""

# Import the math module so that
# we can use math.pi and math.sqrt()
import math

# Get the length from the user and
# convert it to a floating point number.
length = float(input("Length of pendulum (meters): "))

# Compute the time in seconds required for
# the pendulum to swing back and forth.
time = 2 * math.pi * math.sqrt(length / 9.81)

# Display the time rounded to two digits
# after the decimal for the user to see.
print(f"Time (seconds): {time:.2f}")
