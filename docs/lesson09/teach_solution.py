import pandas as pd


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("water.csv", parse_dates=["readDate"])
        print()


        # CORE REQUIREMENTS

        unique(df, "accountType", "Unique account types:")
        unique(df, "meterNumber", "Unique meter numbers:")

        sum_water_used_by_account_type(df)

        count_meters_by_account_type(df)


        # STRETCH CHALLENGES

        sum_water_used_between_dates(df,
                "2018-01-01", "2018-12-31",
                "Water used during 2018:")

        average_water_used_per_dwelling(df)

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def unique(df, column_name, heading):
    """Print all the unique values in a column.

    param df - the data frame that contains the column
    param column_name - name of the column to get the unique values from
    param heading - the heading that will be printed before the unique values
    """
    unique_values = df[column_name].unique()
    print(heading)
    print(len(unique_values), unique_values)
    print()


def sum_water_used_by_account_type(df):
    # Compute and print the total amount of water used.
    total_water_used = df["usage"].sum()
    print("Total water used:", total_water_used)

    # Filter the data frame to readings from residences and
    # compute and print the total water used by residences.
    resfilter = df["accountType"] == "Residence"
    residences = df[resfilter]
    water_used = residences["usage"].sum()
    print("Total water used by residences:", water_used)

    # Filter the data frame to readings from apartment complexes and
    # compute and print the total water used by apartment complexes.
    aptfilter = df["accountType"] == "Apartment Complex"
    apartments = df[aptfilter]
    water_used = apartments["usage"].sum()
    print("Total water used by apartment complexes:", water_used)
    print()


def count_meters_by_account_type(df):
    # Filter the data frame to one row per meter.
    one_row_per_meter = df.drop_duplicates(subset=["meterNumber"])

    # Count and print the number of account types.
    print("Account types:")
    print(one_row_per_meter["accountType"].value_counts())
    print()


def sum_water_used_between_dates(df, start, end, heading):
    # Filter the data frame to readings between start and end.
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    filter = (df["readDate"] >= start) & (df["readDate"] <= end)
    filtered_df = df[filter]

    # Compute and print the amount of water used.
    water_used = filtered_df["usage"].sum()
    print(heading, water_used)


def average_water_used_per_dwelling(df):
    # Filter the data frame to readings in 2018.
    start = pd.to_datetime("2018-01-01")
    end = pd.to_datetime("2018-12-31")
    filter = (df["readDate"] >= start) & (df["readDate"] <= end)
    df2018 = df[filter]

    # Filter the 2018 data frame to one row per meter.
    one_row_per_meter = df2018.drop_duplicates(subset=["meterNumber"], keep="last")

    # Use the filtered data frame from above
    # to compute the number of dwellings.
    number_of_dwells = one_row_per_meter["numberOfDwellings"].sum()
    print("Number of dwellings in 2018:", number_of_dwells)

    # Filter the 2018 data frame to readings
    # for meters that serve dwellings.
    dwelfilter = df2018["numberOfDwellings"] > 0
    reads_for_dwells = df2018[dwelfilter]

    # Compute the total amount of water used during 2018 by dwellings.
    total_for_dwells = reads_for_dwells["usage"].sum()

    # Compute and print the average amount
    # of water used during 2018 per dwelling.
    avg_per_dwell = round(total_for_dwells / number_of_dwells, 2)
    print("Average water used per dwelling in 2018: ", avg_per_dwell)


# If this file was executed like this:
# python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
