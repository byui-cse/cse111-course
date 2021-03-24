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
    students = read_dict("pupils.csv")


    # Get an I-Number from the user.
    inum = str(input("Please enter an I-Number (xx-xxx-xxxx): "))

    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    inum = inum.replace("-", "")

    # Determine if the user input is formatted correctly.
    if not inum.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inum) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inum) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if inum not in students:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                name = students[inum]

                # Print the student name.
                print(name)


def read_dict(filename):
    """Read the contents of a CSV file into a dictionary
    and return the dictionary.

    Parameter filename: the name of the CSV file.
    Return: a new dictionary containing the contents of the CSV file.
    """
    # Create an empty dictionary that will store student
    # information with the I-Number number as the key.
    dictionary = {}

    # Open the specified file for reading and store a reference
    # to the opened file in a variable named infile.
    with open(filename, "rt") as infile:

        # Use the csv module to create a reader object
        # that will read from the opened file.
        reader = csv.reader(infile)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read each row in the CSV file one at a time as a list.
        for row in reader:

            # For the current row, retrieve
            # the values in columns 0 and 1.
            inumber = row[0]
            name = row[1]

            # Add a student's I-Number and name to the dictionary.
            dictionary[inumber] = name

    return dictionary


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
