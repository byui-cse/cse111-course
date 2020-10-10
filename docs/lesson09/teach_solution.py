import pandas as pd


def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])
    print()

    # CORE REQUIREMENTS

    # Print the unique account types.
    acct_types = df["accountType"].unique()
    print("Unique account types:")
    print(len(acct_types), acct_types)
    print()

    # Print the unique meter numbers.
    meters = df["meterNumber"].unique()
    print("Unique meter numbers:")
    print(len(meters), meters)
    print()

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

    # Filter the data frame to one row per meter.
    one_row_per_meter = df.drop_duplicates(subset=["meterNumber"])

    # Count and print the number of account types.
    print("Account types:")
    print(one_row_per_meter["accountType"].value_counts())
    print()

    # STRETCH CHALLENGES

    # Filter the data frame to readings from 2018.
    start = pd.to_datetime("2018-01-01")
    end = pd.to_datetime("2018-12-31")
    filter2018 = (df["readDate"] >= start) & (df["readDate"] <= end)
    df2018 = df[filter2018]

    # Compute and print the amount of water used in 2018.
    water_used = df2018["usage"].sum()
    print("Water used during 2018:", water_used)

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


# Call the main function so that
# this program will start executing.
main()
