# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Write and call functions that demonstrate both
default parameter values and pass by reference.
"""
import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    # Call the append_random_numbers function to
    # add one random number to the numbers list.
    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    # Call the append_random_numbers function to add
    # three random numbers to the numbers list.
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    # Create a list to store random words.
    words = []

    # Call the append_random_words function
    # to add one random word to the list.
    append_random_words(words)
    print(f"words {words}")

    # Call the append_random_words function
    # to add five random words to the list.
    append_random_words(words, 5)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity=1):
    """Append quantity randomly chosen words onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random words that this function
            will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """

    # A list of words to randomly choose from.
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]

    # Randomly choose quantity words and append them onto words_list.
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
