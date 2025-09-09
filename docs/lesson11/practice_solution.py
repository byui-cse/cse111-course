"""
CSE 111
Lesson 11 ICE - Using map and lambda
Author: [Your Name]

Description:
Practice using the map function with lambda expressions in Python to
process lists.

Instructions:
Complete each exercise below by filling in your code using map and
lambda functions.
"""

def main():
    # Exercise 1: Double Each Number
    # Given a list of numbers, use map and lambda to create a new list
    # where each number is doubled.

    numbers_1 = [1, 2, 3, 4, 5]
    # Expected output: [2, 4, 6, 8, 10]

    # TODO: Replace the ... with your code
    doubled_numbers = list(map(lambda x: 2*x, numbers_1))

    print("Exercise 1 - Doubled Numbers:\n", doubled_numbers)


    # Exercise 2: Convert to Uppercase
    # Given a list of strings, use map and lambda to create a new list
    # where each string is converted to uppercase.

    words = ["hello", "world", "python", "map"]
    # Expected output: ["HELLO", "WORLD", "PYTHON", "MAP"]

    # TODO: Replace the ... with your code
    uppercase_words = list(map(lambda word: word.upper(), words))
    print("Exercise 2 - Uppercase Words:\n", uppercase_words)


    # Exercise 3: Calculate the Square
    # Given a list of numbers, use map and lambda to create a new
    # list where each number is squared.

    numbers_2 = [1, 2, 3, 4, 5]
    # Expected output: [1, 4, 9, 16, 25]

    # TODO: Replace the ... with your code
    squared_numbers = list(map(lambda x: x**2, numbers_2))
    print("Exercise 3 - Squared Numbers:\n", squared_numbers)


    # Exercise 4: Find Even Numbers
    # Given a list of numbers, use map and lambda to create a new list
    # of True or False, indicating whether each number is even.

    numbers_3 = [1, 2, 3, 4, 5]
    # Expected output: [False, True, False, True, False]

    # TODO: Replace the ... with your code
    is_even = list(map(lambda x: x%2 == 0, numbers_3))
    print("Exercise 4 - Even Numbers (True/False):\n", is_even)


    # Exercise 5: Combine First and Last Names
    # Given two lists, one with first names and another with last names,
    # use map and lambda to create a new list of full names.

    first_names = ["John", "Jane", "Jim"]
    last_names = ["Doe", "Smith", "Brown"]
    # Expected output: ["John Doe", "Jane Smith", "Jim Brown"]

    # TODO: Replace the ... with your code
    full_names = list(map(lambda first, last: f"{first} {last}", first_names, last_names))
    print("Exercise 5 - Full Names:\n", full_names)


    # Exercise 6: Convert Temperatures
    # Given a list of temperatures in Celsius, use map and lambda to
    # convert each temperature to Fahrenheit.

    temperatures_celsius = [0, 20, 30, 40]
    # Expected output: [32.0, 68.0, 86.0, 104.0]

    # TODO: Replace the ... with your code
    temperatures_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_celsius))
    print("Exercise 6 - Temperatures in Fahrenheit:\n", temperatures_fahrenheit)


    # Exercise 7: Extract the Length of each String
    # Given a list of strings, use map and lambda to create a list of
    # the lengths of each string.

    strings = ["apple", "banana", "cherry"]
    # Expected output: [5, 6, 6]

    # TODO: Replace the ... with your code
    string_lengths = list(map(lambda string: len(string), strings))
    print("Exercise 7 - String Lengths:\n", string_lengths)


    # Exercise 8: Add Corresponding Elements from Two Lists
    # Given two lists of numbers, use map and lambda to create a new
    # list where each element is the sum of the corresponding elements
    # from the two lists.

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    # Expected output: [5, 7, 9]

    # TODO: Replace the ... with your code
    sum_list = list(map(lambda x, y: x + y, list1, list2))
    print("Exercise 8 - Sum of Corresponding Elements:\n", sum_list)


if __name__ == "__main__":
    main()
