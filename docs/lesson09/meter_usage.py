import pandas as pd


def main():
    """
    Use pandas to read the CSV file.
    Get a meter number, a start year, and an end year from the user.
    Use pandas to filter and analyze the data.
    Use matplotlib.pyplot to draw charts to help the user visualize the data.
    """
    pass


def get_int(prompt, lower, upper):
    """Get an integer from the user, validate that the integer is
    between a lower and upper bound, and return the integer to the
    calling function. If the user does not enter an integer between
    lower and upper, inclusive, this function will prompt the user again
    for an integer.

    param prompt: A string to display to the user.
    param lower: The lowest (smallest) integer that the user may enter.
    param upper: The highest (largest) integer that the user may enter.
    """
    pass


def insert_after(ls, existing, toinsert):
    """Insert an element into a list after an existing element."""
    pass


def add_median_usage_column(data):
    """Add to the DataFrame a column named medianUsage
    that contains the median usage grouped by accountType
    and yearMonth and return the new DataFrame.
    """
    data = add_year_month_column(data)
    columns = data.columns.tolist()

    # Find the median usage grouped by accountType and yearMonth.
    medians = data.groupby(["accountType", "yearMonth"]) \
            .aggregate(medianUsage=("usage", "median"))

    # Change the index so that joining the
    # medians with the original data will work.
    data.set_index(["accountType", "yearMonth"], inplace=True)

    # Join the original data and the medians.
    joined = data.join(medians)

    # The join sorts the data by the join key, which is a
    # different order than the CSV file, so sort the rows by
    # meterNumber and readDate like the CSV file, and then reset
    # the index as if the data were just read from the CSV file.
    joined.sort_values(["meterNumber", "readDate"], inplace=True)
    joined.reset_index(drop=False, inplace=True)

    # Reorder the columns to be similar to the CSV file.
    insert_after(columns, "usage", "medianUsage")
    joined = joined[columns]

    # Return the new DataFrame.
    return joined


def add_year_month_column(data):
    """Add to the DataFrame a column named yearMonth that contains only
    the year and the month of the readDate and return the new DataFrame.
    """
    pass


def filter_for_meter(data, meter):
    """Return a new DataFrame that contains only the rows
    where the meterNumber equals the specified meter number.
    """
    pass


def filter_between_dates(data, start, end):
    """Return a new DataFrame that contains only the rows where
    the readDate is between the specified start and end dates.
    """
    pass


def show_meter_usage(indiv, meter):
    """Define a vertical column plot that shows the year
    and month on the x-axis and the usage on the y-axis.

    param indiv: a DataFrame with at least these two
        columns: yearMonth, usage, that is already
        filtered to the rows for one meter number only.
    param meter: the meter number for which indiv is filtered.
    """
    pass


def show_comparison(indiv, meter):
    """Define a line plot that shows the year and month on
    the x-axis and the usage and median usage on the y-axis.

    param indiv: a DataFrame with at least these three
        columns: yearMonth, usage, medianUsage, that is already
        filtered to the rows for one meter number only.
    param meter: the meter number for which indiv is filtered.
    """
    pass


main()
