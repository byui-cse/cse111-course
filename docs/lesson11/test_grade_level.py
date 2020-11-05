from grade_level import level_dict, year_diff, add_columns, grade_level_counts
import collections
from datetime import date
import pandas as pd
import pytest


def test_year_diff():
    """Verify that the year_diff function
    correctly computes age in years.
    """
    baseline1 = date(2016, 2, 29)
    baseline2 = date(2016, 3, 1)
    test_cases = [
        (date(2000,  1, 1), baseline1, 16),
        (date(2000,  2, 1), baseline1, 16),
        (date(2000,  3, 1), baseline1, 15),
        (date(2000,  4, 1), baseline1, 15),
        (date(2000,  5, 1), baseline1, 15),
        (date(2000,  1, 1), baseline2, 16),
        (date(2000,  2, 1), baseline2, 16),
        (date(2000,  3, 1), baseline2, 16),
        (date(2000,  4, 1), baseline2, 15),
        (date(2000,  5, 1), baseline2, 15),
        (baseline1, date(2024,  1, 31), 7),
        (baseline1, date(2024,  2, 29), 8),
        (baseline1, date(2024,  3, 31), 8),
        (baseline1, date(2024,  4, 30), 8),
        (baseline1, date(2024,  5, 31), 8),
        (baseline2, date(2024,  1, 31), 7),
        (baseline2, date(2024,  2, 29), 7),
        (baseline2, date(2024,  3, 31), 8),
        (baseline2, date(2024,  4, 30), 8),
        (baseline2, date(2024,  5, 31), 8)
    ]
    for before, after, expected in test_cases:
        assert year_diff(before, after) == expected


def test_add_columns():
    """Verify that the add_columns function
    correctly adds two columns to a data frame.
    """
    # Read the students.csv file and convert the
    # birthdate column from a string to a datetime64.
    df = pd.read_csv("students.csv", parse_dates=["birthdate"])
    assert len(df) == 187

    # Verify that the data frame doesn't yet have the two columns.
    assert "ageAtCutoff" not in df
    assert "gradeLevel" not in df

    # Create a cutoff date that is 2020 Oct 1.
    cutoff = date(2020, 10, 1)

    # Call the add_columns function which is supposed
    # to add two new columns to the data frame.
    df = add_columns(df, cutoff)

    # Verify that the two columns were added.
    assert "ageAtCutoff" in df
    assert "gradeLevel" in df

    # Because we tested the year_diff function above,
    # we have at least some confidence that it works
    # correctly, so we can use it in this test function.
    ages = [year_diff(bday, cutoff) for bday in df["birthdate"]]
    assert df["ageAtCutoff"].to_list() == ages


def test_grade_level_counts():
    """Verify that the grade_level_counts function correctly counts the
    number of students in each grade (kindergarten, first, second...)
    """
    # Read the students.csv file and convert the
    # birthdate column from a string to a datetime64.
    df = pd.read_csv("students.csv", parse_dates=["birthdate"])
    assert len(df) == 187

    # Create a cutoff date that is 2020 Oct 1.
    cutoff = date(2020, 10, 1)

    # Call the add_columns function so that we
    # can call the grade_level_counts function.
    df = add_columns(df, cutoff)

    # Call the grade_level_counts function.
    levels = grade_level_counts(df)

    # Verify that the new data frame
    # contains the correct number of rows.
    assert len(levels) == 7

    # Verify that the values in the new data frame are correct.
    levels = levels.to_dict()
    counter = dict(collections.Counter(df["ageAtCutoff"].to_list()))
    counter = dict((level_dict[age], count) for age, count in counter.items())
    assert levels == counter


pytest.main(["test_grade_level.py"])
