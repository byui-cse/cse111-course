import pandas as pd
from datetime import date, datetime


def main():
    # Read the students.csv file and convert the
    # birthdate column from a string to a datetime64.
    df = pd.read_csv("students.csv", parse_dates=["birthdate"])

    # Create the cutoff date to be Oct 1 during
    # the current year and print the cutoff date.
    curr_year = date.today().year
    cutoff = date(curr_year, 10, 1)
    print(f"Cutoff date: {cutoff}")
    print()

    df = add_columns(df, cutoff)
    print(df)
    print()

    counts = grade_level_counts(df)
    print(counts)


def add_columns(df, cutoff):
    # Add a column named ageAtCutoff to the data frame. To create the
    # data for the new column, call the apply function on the birthdate
    # column. Pass the year_diff function to the apply function.
    pass

    # Create a lambda function that accepts a student's age
    # as a parameter and uses the level_dict dictionary to
    # find and return the student's grade level.
    pass

    # Add a column named gradeLevel to the data frame. To create the
    # data for the new column, call the apply function on the ageAtCutoff
    # column. Pass the level_from_age function to the apply function.
    pass

    # Return the data frame that contains the two new columns.
    return


# A dictionary to map from ageAtCutoff to gradeLevel.
level_dict = {
# age : grade level
    5 : "kindergarten",
    6 : "first",
    7 : "second",
    8 : "third",
    9 : "fourth",
    10 : "fifth",
    11 : "sixth",
    12 : "seventh",
    13 : "eighth",
    14 : "freshman",
    15 : "sophomore",
    16 : "junior",
    17 : "senior"
}


def year_diff(before: datetime, after: datetime) -> int:
    """Compute and return the difference in years between two dates.

    param before: a datetime object
    param after: another datetime object
    """
    # Ensure that the date in before is earlier
    # than or equal to the date in after.
    if before > after:
        swap = before
        before = after
        after = swap

    # Compute the difference between the two dates in years.
    years = after.year - before.year

    # If necessary, subtract one from the difference.
    if before.month > after.month or \
        (before.month == after.month and before.day > after.day):
        years -= 1

    return years


def grade_level_counts(df):
    """Create and return a new Series that contains
    number of students in each grade level.
    """
    # Call pandas value_counts function to create a new Series named
    # counts that contains the number of students in each grade level.
    pass

    # Return the counts Series.
    return


# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()
