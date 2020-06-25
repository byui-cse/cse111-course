import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("../lesson09/water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])

    # Add to the DataFrame a year column that
    # contains the year from each readDate.
    df["year"] = df["readDate"].dt.year

    show_all_water_usage(df)

    show_water_usage_per_dwelling(df)

    # Show all defined plots.
    plt.show()


def show_all_water_usage(df):
    # For each year, compute the total water usage.
    grouped = df.groupby("year")
    total_df = grouped.aggregate(sumUsage=("usage", "sum"))

    print()
    print("Total usage for all account types (in 1000 gallons):")
    print(total_df)

    barplot = total_df.plot.bar(y="sumUsage")
    plt.tight_layout()


def show_water_usage_per_dwelling(df):
    # Filter the data frame to apartment complexes,
    # residences, trailer courts, and town homes only.
    classes = ["Apartment Complex", "Residence", "Trailer Court", "Town Homes"]
    filter = df["accountType"].isin(classes)
    df = df[filter]

    # For each meterNumber, compute the total water
    # usage and the number of dwellings grouped by year.
    grouped = df.groupby(["meterNumber", "year"])
    interm_df = grouped.aggregate({"usage":"sum", "numberOfDwellings":"mean"})

    # Discard outliers: rows with numDwellings less than 1.
    interm_df = interm_df[interm_df["numberOfDwellings"] >= 1]

    # For each year, compute the total water
    # usage and the total number of dwellings.
    grouped = interm_df.groupby("year")
    final_df = grouped.aggregate({"usage":"sum", "numberOfDwellings":"sum"})

    # Add a computed column that is sumUsage / numDwellings.
    final_df["usagePerDwelling"] = final_df["usage"] / final_df["numberOfDwellings"]

    pd.options.display.float_format = "{:.1f}".format
    print()
    print("Average total usage per dwelling (in 1000 gallons):")
    print(final_df)

    barplot = final_df.plot.bar(y="usagePerDwelling")
    plt.tight_layout()


# Call the main function so that
# this program will start executing.
main()
