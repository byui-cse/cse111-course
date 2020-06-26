import pandas as pd
from datetime import date, datetime


def main():
    # Read the students.csv file and convert the
    # birthdate column from a string to a datetime64.
    df = pd.read_csv("students.csv", parse_dates=["birthdate"])

    # Create the cutoff date to be Oct 1 during the current year.
    curr_year = date.today().year
    cutoff = date(curr_year, 10, 1)

    # Add a column named ageAtCutoff to the data frame. To create the
    # data for the new column, call the apply function on the birthdate
    # column. Pass the year_diff function to the apply function.
    df["ageAtCutoff"] = df["birthdate"].apply(year_diff, args=(cutoff,))

    level_dict = {
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
    level_from_age = lambda age: level_dict[age]
    df["gradeLevel"] = df["ageAtCutoff"].apply(level_from_age)
    print(df)

    # Group by the gradeLevel column and count the
    # number of students in grade level age group.
    grouped = df.groupby("gradeLevel")
    counts = grouped["givenName"].count()

    # Change the name of the counted column from "givenName"
    # to "numberOfStudents" which is more appropriate.
    counts.rename("numberOfStudents")

    counts = counts.reindex(level_dict.values())

    # Print the results on the console.
    print(counts)


def year_diff(before: datetime, after: datetime) -> int:
    """Compute and return the difference in years between two dates.

    param before: a datetime object
    param after: another datetime object
    """
    # Ensure that the date in before is
    # earlier than or equal to the date in after.
    if before > after:
        swap = before
        before = after
        after = swap

    years = after.year - before.year
    if before.month > after.month or \
        (before.month == after.month and before.day > after.day):
        years -= 1
    return years


# Call the main function so that
# this program will start executing.
main()
