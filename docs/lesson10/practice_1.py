# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
This program reads assignment scores from a text file
and computes and prints the average of the test scores.
"""
import statistics

def main():
    # TODO: Put all the code in the main function inside one try block.

        # Get a file name from the user.
        filename = input("Enter the name of the scores text file: ")

        # Create an empty list that will store all the scores.
        scores_list = []

        linenum = 0
        with open(filename, "rt") as scores_file:

            # For each line of text in the file:
            #     Convert the text to a floating point number.
            #     Add the floating point number to the list of scores.
            for text in scores_file:
                linenum += 1
                score = float(text.strip())
                scores_list.append(score)

        # Call the statistics.mean function
        # to compute the average score.
        avg = statistics.mean(scores_list)

        # Print the average score rounded to
        # one digit after the decimal point.
        print(f"{avg:.1f}")

    # TODO: At the end of the main function, add one except block for
    # each of the following error types. Each except block should
    # contain one print statement that prints a helpful error message
    # for the user.
    # 1. FileNotFoundError
    # 2. PermissionError
    # 3. ValueError
    # 4. ZeroDivisionError


# If this file was executed like this:
# > python example.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
