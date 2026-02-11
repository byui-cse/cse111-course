"""
CSE 111
Lesson 02 - Calling Functions
Author: [Your Name Here]

Description:
Practice calling built-in functions and standard library functions.

Instructions:
Write a program that:

1. Asks the user to enter a sentence.
   - Prints the length of the sentence.
   - Prints the sentence in uppercase.
   - Prints the sentence in lowercase.
   - Prints the number of words in the sentence.
     (Hint: Use .split() and len())

2. Asks the user to enter a number.
   - Prints the square root of the number.
   - Prints the number rounded to 2 decimal places.
   - Prints the absolute value of the number.

3. (Stretch) Ask for two numbers and check if they are
   close using math.isclose() with abs_tol=0.01.
"""

# Import necessary module
import math

# Step 1: Ask the user to enter a sentence.
sentence = input("Enter a sentence: ")
length = len(sentence)
uppercase = sentence.upper()
lowercase = sentence.lower()
words = sentence.split()
num_words = len(words)
print(f"Length of sentence: {length}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Number of words: {num_words}")

# Step 2: Ask the user to enter a number.
number = float(input("Enter a number: "))
sqrt_value = math.sqrt(abs(number))
rounded = round(number, 2)
abs_val = abs(number)
print(f"Square root of absolute value: {sqrt_value:.2f}")
print(f"Rounded number: {rounded}")
print(f"Absolute value: {abs_val}")

# (Stretch) Step 3: Ask for two numbers and check if they are close
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if math.isclose(num1, num2, abs_tol=0.01):
    print(f"{num1} and {num2} are close.")
else:
    print(f"{num1} and {num2} are not close.")
