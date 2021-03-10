"""
This program asks the user for
1) the name of a text file
2) a line number
and prints the text from that line of the file.
"""

def main():
    try:
        # Get a filename from the user.
        filename = input("Enter the name of text file: ")

        # Open the text file for reading.
        with open(filename, "rt") as infile:

            # Read all the lines of the text file into a list.
            string = infile.read()
            lines = string.splitlines()

        # Get a line number from the user.
        linenum = int(input("Enter a line number: "))

        # Get the line that the user requested from the list.
        line = lines[linenum - 1]

        # Print the line that the user requested.
        print()
        print(line)

    except FileNotFoundError as file_not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(file_not_found_err).__name__, file_not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the name of an existing file.")

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for the line number.")

    except IndexError as index_err:
        # This code will be executed if the user enters a valid integer
        # for the line number, but the integer is negative or the
        # integer is greater than the number of lines in the file.
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        if linenum < 0:
            print(f"{linenum} is a negative integer.")
        else:
            print(f"{linenum} is greater than the number of lines in {filename}.")
            print(f"There are only {len(lines)} lines in {filename}.")
        print(f"Run the program again and enter a line number between 1 and {len(lines)}.")

    except Exception as excep:
        # This code will be executed if some other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")


# Call the main function so that
# this program will start executing.
main()
