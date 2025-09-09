"""
CSE 111
Lesson 04 ICE - Functions with Parameters
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
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

# Example Usage:
print(add(5, 3))  # Should print 8
print(sub(5, 3))  # Should print 2
print(mult(5, 3)) # Should print 15
print(div(5,3))   # Should print 1.67


# 2. String Repeater
# Write a function named "repeat_string" that takes two parameters:
# a string and an integer named "n". The function should return the
# string repeated `n` times.

def repeat_string(string, n):
    return string * n

# Example Usage:
print(repeat_string("Hello", 3))  # Should print "HelloHelloHello"
print(repeat_string("Bob", 5))  # Should print "BobBobBobBobBob"


# 3. Compound Interest
# Write a function named "compound_interest" that calculates and returns
# compound interest based on principal, rate, and time (in years). Use
# the formula:  A = P * (1 + r)**t.

def compound_interest(principal, rate, time):
    future_val = principal * (1 + rate)**time
    return round(future_val, 2)

# Example Usage:
print(compound_interest(1000, 0.05, 5))  # Should print the total amount
                                         # after 5 years which is 1276.28


# 4. Password Validator
# Write a function named "validate_password" that takes a password
# (string) as a parameter. Check if the password meets the following
# criteria:
# - At least 8 characters
# - Contains both letters and numbers
# Return True if valid, False otherwise.

def validate_password(password):
    # First make sure it meets length requirement
    if len(password) < 8:
        return False

    # First way to check for digits and letters
    has_letter = False
    has_digit = False
    for letter in password:
        if letter.isalpha():
            has_letter = True
        elif letter.isdigit():
            has_digit = True

    return has_letter and has_digit

    # # Alternative way to check for digits and letters
    # return any(letter.isdigit() for letter in password) \
    #        and any(letter.isalpha() for letter in password)

# Example Usage:
print(validate_password("pass1234"))  # Should print True
print(validate_password("password1")) # Should print True
print(validate_password("pass"))      # Should print False
print(validate_password("pass12"))    # Should print False
print(validate_password("passwords")) # Should print False
print(validate_password("123456789")) # Should print False


# 5. Distance Between Two Points
# Write a function named "calculate_distance" that takes four parameters:
# x1, y1, x2, y2 representing the coordinates of two points.
# The function must calculate and return the distance between the two
# points using the formula:
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Example Usage:
print(calculate_distance(1, 2, 4, 6))  # Should print the distance between
                                       # points (1, 2) and (4, 6), which is 5.0
