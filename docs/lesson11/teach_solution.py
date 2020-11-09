import pandas as pd
from datetime import date, datetime


def main():
    try:
        # Read the students.csv file and convert the
        # birthdate column from a string to a datetime64.
        df = pd.read_csv("students.csv", parse_dates=["birthdate"])

        # Create the cutoff date to be Oct 1 during
        # the current year and print the cutoff date.
        curr_year = date.today().year
        cutoff = date(curr_year, 10, 1)
        print(f"Cutoff date: {cutoff}")
        print()

        # Call the add_columns function and print
        # the data frame with the two new columns.
        df = add_columns(df, cutoff)
        print(df)
        print()

        # Call the grade_level_counts function
        # and print the new counts data frame.
        counts = grade_level_counts(df)
        print(counts)

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def add_columns(df, cutoff):
    # Add a column named ageAtCutoff to the data frame. To create the
    # data for the new column, call the apply function on the birthdate
    # column. Pass the year_diff function to the apply function.
    df["ageAtCutoff"] = df["birthdate"].apply(year_diff, args=(cutoff,))

    # Create a lambda function that accepts a student's age
    # as a parameter and uses the level_dict dictionary to
    # find and return the student's grade level.
    level_from_age = lambda age: level_dict[age]

    # Add a column named gradeLevel to the data frame. To create the
    # data for the new column, call the apply function on the ageAtCutoff
    # column. Pass the level_from_age function to the apply function.
    df["gradeLevel"] = df["ageAtCutoff"].apply(level_from_age)

    # Sort the data frame by age at cutoff, surname, and given name.
    df.sort_values(["ageAtCutoff", "surname", "givenName"], inplace=True)

    # Return the data frame that contains the two new columns.
    return df


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
        before, after = after, before
        #swap = before
        #before = after
        #after = swap

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
    counts = df["gradeLevel"].value_counts(sort=False)

    # The value_counts function orders the grade levels in the
    # order that they are found in the original data frame which is
    # probably not the order that a user wants to see them. Reorder
    # the grade levels to be the same order as the level_dict.
    counts = counts.reindex(level_dict.values(), copy=False)

    # The reindex function may add rows which
    # have no count, so drop those rows.
    counts.dropna(inplace=True)

    # The reindex function may change the counts from
    # integers to floats, so change them back to integers.
    counts = counts.astype(int, copy=False)

    # Return the counts Series.
    return counts


# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()
