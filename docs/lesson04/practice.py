"""
CSE 111
Lesson 4 - Functions with Parameters
Author: [Your Name Here]

Description:
Practice writing functions with parameters using the exercises below

Instructions:
Complete each of the functions below.
"""
# 1. Simple Calculator Functions
# Write functions for the basic math operations: add, subtract, multiply,
# and divide. Each function should take two parameters (numbers) and
# return the result.

def add(a, b):
    # Your code here
    ...

def sub(a, b):
    # Your code here
    ...

def mult(a, b):
    # Your code here
    ...

def div(a, b):
    # Your code here
    ...


# 2. String Repeater
# Write a function named "repeat_string" that takes two parameters:
# a string and an integer named "n". The function should return the
# string repeated `n` times.

def repeat_string(string, n):
    # Your code here
    ...


# 3. Compound Interest
# Write a function named "compound_interest" that calculates and returns
# compound interest based on principal, rate, and time (in years). Use
# the formula:  A = P * (1 + r)**t.

def compound_interest(principal, rate, time):
    # Your code here
    ...


# 4. Password Validator
# Write a function named "validate_password" that takes a password
# (string) as a parameter. Check if the password meets the following
# criteria:
# - At least 8 characters
# - Contains both letters and numbers
# Return True if valid, False otherwise.

def validate_password(password):
    # Your code here
    ...


# 5. Distance Between Two Points
# Write a function named "calculate_distance" that takes four parameters:
# x1, y1, x2, y2 representing the coordinates of two points.
# The function must calculate and return the distance between the two
# points using the formula:
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

import math
def calculate_distance(x1, y1, x2, y2):
    # Your code here
    ...


# Example Usage:
def main():
    print(add(5, 3))  # Should print 8
    print(sub(5, 3))  # Should print 2
    print(mult(5, 3)) # Should print 15
    print(div(5,3))   # Should print 1.67

    print(repeat_string("Hello", 3))  # Should print "HelloHelloHello"
    print(repeat_string("Bob", 5))  # Should print "BobBobBobBobBob"

    print(compound_interest(1000, 0.05, 5))  # Should print the total amount after 5 years

    print(validate_password("pass1234"))  # Should print True
    print(validate_password("password1")) # Should print True
    print(validate_password("pass"))      # Should print False
    print(validate_password("pass12"))    # Should print False
    print(validate_password("passwords")) # Should print False
    print(validate_password("123456789")) # Should print False

    print(calculate_distance(1, 2, 4, 6))  # Should print the distance between
                                           # points (1, 2) and (4, 6), which is 5.0


main()
