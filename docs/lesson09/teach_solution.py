import pandas as pd


def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("water.csv",
            dtype={"meterNumber":"str",
                "readDate":"str", "numberOfDays":"int_",
                "reading":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])
    print()

    # CORE REQUIREMENTS

    # Print the list of unique account types.
    acct_types = data["accountType"].unique()
    print("Unique account types:")
    print(len(acct_types), acct_types)
    print()

    # Print the list of unique meter numbers.
    meters = data["meterNumber"].unique()
    print("Unique meter numbers:")
    print(len(meters), meters)
    print()

    # Compute and print the total amount of water used.
    total_water_used = data["usage"].sum()
    print("Total water used:", total_water_used)

    # Filter the list to readings from residences and
    # compute and print the total water used by residences.
    residences = data[data["accountType"] == "Residence"]
    water_used = residences["usage"].sum()
    print("Total water used by residences:", water_used)

    # Filter the list to readings from apartment complexes and
    # compute and print the total water used by apartment complexes.
    complexes = data[data["accountType"] == "Apartment Complex"]
    water_used = complexes["usage"].sum()
    print("Total water used by apartment complexes:", water_used)
    print()

    # Filter the data to one row per meter.
    one_row_per_meter = data.drop_duplicates(subset=["meterNumber"])

    # Count and print the number of account types.
    print("Account types:")
    print(one_row_per_meter["accountType"].value_counts())
    print()

    # STRETCH CHALLENGES

    # Filter the data to readings from 2014.
    start = pd.to_datetime("2014-01-01")
    end = pd.to_datetime("2014-12-31")
    data2014 = data[(data["readDate"] >= start) & (data["readDate"] <= end)]

    # Compute and print the amount of water used in 2014.
    water_used = data2014["usage"].sum()
    print("Water used during 2014:", water_used)

    # Filter the 2014 data to one row per meter.
    one_row_per_meter = \
        data2014.drop_duplicates(subset=["meterNumber"], keep="last")

    # Use the filtered data from above to compute the number of dwellings.
    number_of_dwells = one_row_per_meter["numberOfDwellings"].sum()
    print("Number of dwellings in 2014:", number_of_dwells)

    # Filter the 2014 data to readings for meters that serve dwellings.
    reads_for_dwells = data2014[data2014["numberOfDwellings"] > 0]

    # Compute the total amount of water used during 2014 by dwellings.
    total_for_dwells = reads_for_dwells["usage"].sum()

    # Compute and print the average amount
    # of water used during 2014 by dwellings.
    avg_per_dwell = round(total_for_dwells / number_of_dwells, 2)
    print("Average water used by each dwelling in 2014: ", avg_per_dwell)


main()
