# example.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

"""
This program reads assignment scores from a text file
and computes and prints the average of the test scores.
"""
import statistics

def main():
    try:
        # Get a file name from the user.
        filename = input("Enter the name of the scores text file: ")

        # Create an empty list that will store all the scores.
        scores = []

        linenum = 0
        with open(filename, "rt") as scores_file:

            # For each line of text in the file:
            #     Convert the text to a floating point number.
            #     Add the floating point number to the list of scores.
            for text in scores_file:
                linenum += 1
                score = float(text)
                scores.append(score)

        # Call the statistics.mean function to compute the average score.
        avg = statistics.mean(scores)

        # Print the average score rounded to
        # one digit after the decimal point.
        print(f"{avg:.1f}")

    except FileNotFoundError as file_not_found_err:
        print(f"Error: {filename} does not exist.")
    except PermissionError as perm_err:
        print(f"Error: your account does not have permission to read {filename}.")
    except ValueError as val_err:
        print(f"Error: invalid score in {filename} at line {linenum}.")
    except ZeroDivisionError as zero_div_err:
        print(f"Error: {filename} is empty.")
    except Exception as excep:
        print(type(excep).__name__, excep, sep=": ")


# If this file was executed like this:
# > python example.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
