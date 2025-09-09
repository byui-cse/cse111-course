"""
CSE 111
Lesson 03 ICE - Writing and Calling Functions
Author: [Your Name Here]

Description:
Practice writing and calling a function that takes a string parameter
and returns a result.

Instructions:
Write a program that:
  1. Contains a main() function that:
     - Asks the user to enter a singular noun (e.g., dog, party, box)
     - Calls make_plural(word) to compute the plural form of the word.
     - Prints the plural form.
  2. Contains one user-defined function named "make_plural(word)" that
     returns the plural version of a word.
     - If the word ends with 'y' --> replace 'y' with 'ies'
     - If the word ends with 's', 'x', 'z', 'ch', or 'sh' --> add 'es'
     - Otherwise --> add 's'
  3. make_plural should not include an input statement (keep that in main()).
  4  make_plural should not print anything. It should return a string.
  5. Only main() should print.
  6. Include a call to main() at the bottom of the file.
  7. Stretch #1 - Enhance your make_plural function to also handle words
     that end in 'f' and 'fe'.
     - If the word ends with 'f' --> replace 'f' with 'ves'
     - If the word ends with 'fe' --> replace 'fe' with 'ves'
  8. Stretch #2 - Handle irregular plural words, such as child, man,
     woman, mouse, goose, tooth, foot, and any others you can think of.
     (Hint: make a dictionary to handle these irregular words).
"""

# Define the main function.
def main():
    singular = input("Enter a singular noun: ")
    plural = make_plural(singular)
    print(f"Plural form: {plural}")


def make_plural(word):
    """Return the plural form of the given word."""
    irregulars = {
        "child": "children",
        "man": "men",
        "woman": "women",
        "mouse": "mice",
        "goose": "geese",
        "tooth": "teeth",
        "foot": "feet"
    }

    if word in irregulars:
        return irregulars[word]
    elif word.endswith("fe"):
        return word[:-2] + "ves"
    elif word.endswith("f"):
        return word[:-1] + "ves"
    elif word.endswith("y"):
        return word[:-1] + "ies"
    elif (word.endswith("s") or word.endswith("x") or word.endswith("z") or
          word.endswith("ch") or word.endswith("sh")):
        return word + "es"
    else:
        return word + "s"


main()
