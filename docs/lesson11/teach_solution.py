# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    try:
        # Read the pupils.csv file into a compound list.
        students_list = read_compound_list("pupils.csv")

        # As a debugging aid, print the students_list.
        #print(students_list)

        sorted_list_1 = sort_oldest_to_youngest(students_list)
        print("Ordered from Oldest to Youngest")
        print_list(sorted_list_1)

        sorted_list_2 = sort_by_given_name(students_list)
        print("Ordered by Given Name")
        print_list(sorted_list_2)

        sorted_list_3 = sort_by_birth_month_day(students_list)
        print("Ordered by Birth Month and Day")
        print_list(sorted_list_3)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def sort_oldest_to_youngest(students_list):
    """Sort a list of students by their birthdate.

    Parameter
        students_list: a list that contains small lists.
            Each small list contains the given name,
            surname, and birthdate of one student.
    Return: a new list of students that is sorted by birthdate.
    """
    # Define a lambda function that extracts a student's birthdate.
    extract_birthdate = lambda student: student[BIRTHDATE_INDEX]

    # Call the sorted function to sort the
    # list of students by their birthdate.
    sorted_list = sorted(students_list, key=extract_birthdate)

    # Return the sorted list.
    return sorted_list


def sort_by_given_name(students_list):
    """Sort a list of students by their given name.

    Parameter
        students_list: a list that contains small lists.
            Each small list contains the given name,
            surname, and birthdate of one student.
    Return: a new list of students that is sorted by given name.
    """
    # Define a lambda function that extracts a student's given name.
    extract_given_name = lambda student: student[GIVEN_NAME_INDEX]

    # Call the sorted function to sort the
    # list of students by their given name.
    sorted_list = sorted(students_list, key=extract_given_name)

    # Return the sorted list.
    return sorted_list


def sort_by_birth_month_day(students_list):
    """Sort a list of students by their birth month and day.
    In other words sort the list by their birthdate but ignore
    the year of their birthdate.

    Parameter
        students_list: a list that contains small lists.
            Each small list contains the given name,
            surname, and birthdate of one student.
    Return: a new list of students that is sorted by birth
        month and day.
    """
    # Define a nested function that extracts
    # a student's birthdate without the year.
    def extract_month_and_day(student):
        birthdate_string = student[BIRTHDATE_INDEX]
        month_and_day = birthdate_string[5:]
        return month_and_day

    # Call the sorted function to sort the list
    # of students by their birth month and day.
    sorted_list = sorted(students_list, key=extract_month_and_day)

    # Return the sorted list.
    return sorted_list


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(compound_list):
    """Print the elements in a compound list to
    the terminal window for the user to see.

    Parameter
        compound_list: a list that contains other lists
    Return: nothing
    """
    for element in compound_list:
        print(element)
    print()


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
