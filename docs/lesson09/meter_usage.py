import pandas as pd


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.

        # Add a yearMonth and a medianUsage column to the DataFrame.

        # Repeat as necessary.

            # Get a meter number from the user.

            # Get a start year and an end year from the user.

            # Convert the start and end years from integers to dates.

            # Filter the DataFrame to the meter number
            # and years specifified by the user.

            # Define two plots.

            # Show all defined plots.
        pass

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def get_int(prompt, lower, upper):
    """Get an integer from the user, validate that the integer is
    between a lower and upper bound, and return the integer to the
    calling function. If the user enters text that cannot be converted
    to an integer or if the converted integer is not between lower and
    upper inclusive, this function will prompt the user repeatedly until
    the user enters an integer between lower and upper.

    param prompt: A string to display to the user.
    param lower: The lowest (smallest) integer that the user may enter.
    param upper: The highest (largest) integer that the user may enter.
    return: The integer that the user entered.
    """
    return


def add_median_usage_column(df):
    """Add to a DataFrame a column named medianUsage that contains
    the median usage grouped by accountType and yearMonth.

    param df: The DataFrame that this function will add a column to.
    return: A new DataFrame that contains a medianUsage column.
    """
    df = add_year_month_column(df)

    # Find the median usage grouped by accountType and yearMonth.
    columns = ["accountType", "yearMonth"]
    group = df.groupby(columns)
    median_df = group.aggregate(medianUsage=("usage", "median"))

    # Join the original data frame and the median data frame.
    joined_df = df.join(median_df, on=columns)
    return joined_df


def add_year_month_column(df):
    """Add to a DataFrame a column named yearMonth that contains only
    the year and the month of the readDate and return the new DataFrame.

    param df: The DataFrame that this function will add a column to.
    return: The DataFrame that contains a yearMonth column.
    """
    return


def filter_for_meter(df, meter_number):
    """Return a new DataFrame that contains only the rows where
    the meterNumber column equals the parameter meter_number.

    param df: The DataFrame that this function will filter.
    param meter_number: df will be filtered so that all the rows in the
        new DataFrame will have this meter number.
    return: A new DataFrame that contains rows for meter_number only.
    """
    return


def filter_between_dates(df, start, end):
    """Return a new DataFrame that contains only the rows where the
    readDate column is between the specified start and end dates.

    param df: The DataFrame that this function will filter.
    param start: A date object. This function will filter df so that all
        the rows in the new DataFrame have a readDate greater than or
        equal to this date.
    param end: A date object. This function will filter df so that all
        the rows in the new DataFrame have a readDate less than or equal
        to this date.
    return: A new DataFrame that contains only rows where the readDate
        is between start and end inclusive.
    """
    return


def show_meter_usage(indiv_df, meter_number):
    """Define a vertical column plot that shows the year
    and month on the x-axis and the usage on the y-axis.

    param indiv_df: A DataFrame with at least two columns: yearMonth and
        usage. The DataFrame must already be filtered to the rows for
        only one meter number before it is passed into this function.
    param meter_number: The meter number for which df is already filtered.
    return: Nothing
    """
    pass


def show_comparison(indiv_df, meter_number):
    """Define a line plot that shows the year and month on
    the x-axis and the usage and median usage on the y-axis.

    param indiv_df: A DataFrame with at least three columns: yearMonth, usage
        and medianUsage. The DataFrame must already be filtered to the rows
        for only one meter number before it is passed into this function.
    param meter_number: The meter number for which df is already filtered.
    return: Nothing
    """
    pass


# If this file was executed like this:
# python meter_usage.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
