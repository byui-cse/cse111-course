from meter_usage import get_int, insert_after, \
        add_year_month_column, filter_for_meter, filter_between_dates
from io import StringIO
import pandas as pd
import pytest
import sys


def test_get_int(monkeypatch):
    """Verify that the get_int function does not return a value
    until the user input is between the minimum and maximum values.
    """
    # Setup simulated user input: hi, -8, 10, and 2
    test_input = StringIO("hi\n-8\n10\n2\n")
    monkeypatch.setattr(sys, "stdin", test_input)

    assert get_int("Please enter an integer: ", -5, 5) == 2


def test_insert_after():
    """Verify that the insert after function
    correctly inserts elements into a list.
    """
    test_cases = [
        (["a"], "a", "b", ["a", "b"]),
        (["a", "c"], "a", "b", ["a", "b", "c"]),
        (["a", "b"], "b", "d", ["a", "b", "d"])
    ]
    for test_case in test_cases:
        alist = test_case[0]
        existing = test_case[1]
        toinsert = test_case[2]
        expected = test_case[3]
        result = insert_after(alist, existing, toinsert)
        assert result == expected


def test_add_year_month_column():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])
    assert len(df) == 246830

    # Ensure that the data frame doesn't have a column named yearMonth.
    assert "yearMonth" not in df

    # Call the add_year_month_column function.
    df = add_year_month_column(df)

    # Ensure that the data frame now has a column named yearMonth.
    assert "yearMonth" in df

    # Ensure that each cell in the yearMonth column
    # contains a period[M] with a valid year and month.
    for cell in df["yearMonth"]:
        year = cell.year
        month = cell.month
        assert 2015 <= cell.year <= 2019
        assert 1 <= cell.month <= 12


def test_filter_for_meter():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])
    assert len(df) == 246830

    # Call the filter_for_meter function.
    meter_number = "M4724"
    df = filter_for_meter(df, meter_number)

    # Because the only rows remaining in the data
    # frame should be for meter M4724, verify that
    # the meter number is M4724 in all rows.
    assert len(df) == 60
    for cell in df["meterNumber"]:
        assert cell == "M4724"


def test_filter_between_dates():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])
    assert len(df) == 246830

    # Call the filter_between_dates function.
    start = pd.to_datetime(f"2016-07-01")
    end = pd.to_datetime(f"2016-07-31")
    df = filter_between_dates(df, start, end)

    # Verify that the read date in all remaining
    # rows is between the start and end dates.
    assert len(df) == 4041
    for cell in df["readDate"]:
        assert start <= cell <= end


pytest.main(["-v", "--tb=no", "test_meter_usage.py"])
