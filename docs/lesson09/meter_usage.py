import pandas as pd


def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.

    # Add a yearMonth and a medianUsage column to the DataFrame.

    # Repeat as necessary.

        # Get a meter number from the user.

        # Get start and end years from the user.

        # Convert the start and end years
        # from integers to date strings.

        # Filter the DataFrame to the meter number
        # and years specifified by the user.

        # Define two plots.

        # Show all defined plots.
    pass


def get_int(prompt, lower, upper):
    """Get an integer from the user, validate that the integer is
    between a lower and upper bound, and return the integer to the
    calling function. If the user does not enter an integer between
    lower and upper, inclusive, this function will prompt the user
    again for an integer.

    param prompt: A string to display to the user.
    param lower: The lowest (smallest) integer that the user may enter.
    param upper: The highest (largest) integer that the user may enter.
    """
    pass


def insert_after(ls, existing, toinsert):
    """Insert an element into a list after an existing element."""
    pass


def add_median_usage_column(df):
    """Add to the DataFrame a column named medianUsage that
    contains the median usage grouped by accountType and yearMonth.
    Return the new DataFrame.
    """
    df = add_year_month_column(df)
    columns = df.columns.tolist()

    # Find the median usage grouped by accountType and yearMonth.
    median_df = df.groupby(["accountType", "yearMonth"]) \
            .aggregate(medianUsage=("usage", "median"))

    # Change the index so that joining the median_df
    # with the original data frame will work.
    df.set_index(["accountType", "yearMonth"], inplace=True)

    # Join the original data frame and the median data frame.
    joined_df = df.join(median_df)

    # The join sorts the data frame by the join key, which is
    # a different order than the CSV file, so sort the rows by
    # meterNumber and readDate like the CSV file, and then reset
    # the index as if the data were just read from the CSV file.
    joined_df.sort_values(["meterNumber", "readDate"], inplace=True)
    joined_df.reset_index(drop=False, inplace=True)

    # Reorder the columns to be similar to the CSV file.
    insert_after(columns, "usage", "medianUsage")
    joined_df = joined_df[columns]

    return joined_df


def add_year_month_column(df):
    """Add to the DataFrame a column named yearMonth that contains only
    the year and the month of the readDate and return the new DataFrame.
    """
    pass


def filter_for_meter(df, meter):
    """Return a new DataFrame that contains only the rows
    where the meterNumber equals the parameter meter.
    """
    pass


def filter_between_dates(df, start, end):
    """Return a new DataFrame that contains only the rows where
    the readDate is between the specified start and end dates.
    """
    pass


def show_meter_usage(df, meter):
    """Define a vertical column plot that shows the year
    and month on the x-axis and the usage on the y-axis.

    param df: a DataFrame with at least these two
        columns: yearMonth, usage, that is already
        filtered to the rows for one meter number only.
    param meter: the meter number for which df is filtered.
    """
    pass


def show_comparison(df, meter):
    """Define a line plot that shows the year and month on
    the x-axis and the usage and median usage on the y-axis.

    param df: a DataFrame with at least these three columns:
        yearMonth, usage, medianUsage, that is already
        filtered to the rows for one meter number only.
    param meter: the meter number for which df is filtered.
    """
    pass


# Call the main function so that
# this program will start executing.
main()
