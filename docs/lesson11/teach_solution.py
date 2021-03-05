import pandas as pd
from datetime import date


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
    """Add two columns named "ageAtCutoff" and "gradeLevel" to a
    DataFrame and return the DataFrame with the new columns.

    param df: The DataFrame to add two columns to
    param cutoff: A date to use when computing the values in the
        ageAtCutoff column.
    return: The DataFrame with the two new columns.
    """
    # Add a column named ageAtCutoff to the data frame. To create the
    # data for the new column, call the apply function on the birthdate
    # column. Pass the year_diff function and the args named parameter
    # to the apply function.
    df["ageAtCutoff"] = df["birthdate"].apply(year_diff, args=(cutoff,))

    # Create a lambda function and store it in a variable named
    # level_from_age. The lambda function must accept a student's
    # age as a parameter and use the level_dict dictionary to find
    # and return the student's grade level.
    level_from_age = lambda age: level_dict[age]

    # Add a column named gradeLevel to the data frame. To create
    # the data for the new column, call the apply function on the
    # ageAtCutoff column. Pass the level_from_age lambda function
    # to the apply function.
    df["gradeLevel"] = df["ageAtCutoff"].apply(level_from_age)

    # Return the data frame that contains the two new columns.
    return df


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


def year_diff(before, after):
    """Compute and return the difference in years between two dates.

    param before: a datetime object
    param after: another datetime object
    return: an integer
    """
    # Ensure that the date in before is earlier
    # than or equal to the date in after.
    if before > after:
        before, after = after, before

    # Compute the difference between the two dates in years.
    years = after.year - before.year

    # If necessary, subtract one from the difference.
    if before.month > after.month or \
        (before.month == after.month and before.day > after.day):
        years -= 1

    return years


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
