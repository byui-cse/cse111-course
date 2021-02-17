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
        with open(filename, "rt") as infile:

            # For each line of text in the file:
            #     Convert the text to a floating point number.
            #     Add the floating point number to the list of scores.
            for text in infile:
                linenum += 1
                score = float(text)
                scores.append(score)

        # Call the statistics.mean function to compute the average score.
        avg = statistics.mean(scores)

        # Round the average to one digit after the decimal point.
        rounded = round(avg, 1)

        # Print the rounded average score.
        print(rounded)

    except FileNotFoundError as ex:
        print(f"Error: {filename} does not exist.")
    except PermissionError as ex:
        print(f"Error: your account does not have permission to read {filename}.")
    except ValueError as ex:
        print(f"Error: invalid score in {filename} at line {linenum}.")
    except ZeroDivisionError as ex:
        print(f"Error: {filename} is empty.")
    except Exception as ex:
        print(type(ex).__name__, ex, sep=": ")


# Call the main function so that
# this program will start executing.
main()
