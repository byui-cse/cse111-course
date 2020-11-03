"""This program asks the user for
1) the name of a text file
2) a line number
and prints the text from that line of the file.
"""

def main():
    try:
        # Get a filename and line number from the user.
        filename = input("Enter the name of text file: ")
        linenum = int(input("Enter a line number: "))

        # Open the text file for reading.
        with open(filename, "rt") as infile:

            # Read all the lines of the text file into a list.
            lines = infile.readlines()

        # Get the line that the user requested from the list.
        line = lines[linenum - 1]

        # Print the line that the user requested.
        print()
        print(line)

    except FileNotFoundError as ex:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(ex).__name__, ex, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the name of an existing file.")

    except ValueError as ex:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(ex).__name__, ex, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for the line number.")

    except IndexError as ex:
        # This code will be executed if the user enters a
        # valid integer for the line number, but the integer
        # is greater than the number of lines in the file.
        print()
        print(type(ex).__name__, ex, sep=": ")
        print(f"{linenum} is greater than the number of lines in {filename}.")
        print(f"There are only {len(lines)} lines in {filename}.")
        print(f"Run the program again and enter a line number between 1 and {len(lines)}.")

    except Exception as ex:
        # This code will be executed if some other type of exception occurs.
        print()
        print(type(ex).__name__, ex, sep=": ")


# Call the main function so that
# this program will start executing.
main()
