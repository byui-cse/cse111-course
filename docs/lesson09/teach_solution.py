"""
A common task for many knowledge workers is to use a number, key, or ID
to look up information about a person. For example, a knowledge worker
may use a phone number or e-mail address as a key to find (or look up)
additional information about a customer. During this activity, your team
will write a Python program that uses a student's I-Number to look up
the student's name.
"""
import csv


def main():
    # The column headings and indexes.
    I_NUMBER = 0
    NAME = 1

    # Read the contents of a CSV file named students.csv
    # into a dictionary named students. Use the I-Number
    # as the key in the dictionary.
    students = read_dict("students.csv", I_NUMBER)

    # Get an I-Number from the user.
    inumber = str(input("Please enter an I-Number (xx-xxx-xxxx): "))

    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    inumber = inumber.replace("-", "")

    # Determine if the user input is formatted correctly.
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if inumber not in students:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = students[inumber]
                name = value[NAME]

                # Print the student name.
                print(name)


def read_dict(filename, key_column_index):
    """Read the contens of a CSV file into a dictionary
    and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(text_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row

    # Return the dictionary.
    return dictionary


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
