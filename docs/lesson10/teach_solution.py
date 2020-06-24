import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("../lesson09/water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])

    # Add to the DataFrame a year column
    # that contains the year of each reading.
    data["year"] = data["readDate"].dt.year

    show_all_water_usage(data)

    show_water_usage_per_dwelling(data)

    # Show all defined plots.
    plt.show()


def show_all_water_usage(data):
    # For each year, compute the total water usage.
    grouped = data.groupby("year")
    totals = grouped.aggregate(sumUsage=("usage", "sum"))

    print()
    print("Total usage for all account types (in 1000 gallons):")
    print(totals)

    barplot = totals.plot.bar(y="sumUsage")
    plt.tight_layout()


def show_water_usage_per_dwelling(data):
    # Filter the data to apartment complexes,
    # residences, trailer courts, and town homes.
    classes = ["Apartment Complex", "Residence", "Trailer Court", "Town Homes"]
    data = data[data["accountType"].isin(classes)]

    # For each meterNumber, compute the total water
    # usage and the number of dwellings grouped by year.
    grouped = data.groupby(["meterNumber", "year"])
    interm = grouped.aggregate(
                sumUsage=("usage", "sum"),
                numDwellings=("numberOfDwellings", "mean"))

    # Discard outliers: rows with numDwellings less than 1.
    interm = interm[interm["numDwellings"] >= 1]

    # For each year, compute the total water
    # usage and the total number of dwellings.
    final = interm.groupby("year").aggregate(
                sumUsage=("sumUsage", "sum"),
                numDwellings=("numDwellings", "sum"))

    # Add a computed column that is sumUsage / numDwellings.
    final["usagePerDwelling"] = final["sumUsage"] / final["numDwellings"]

    pd.options.display.float_format = "{:.1f}".format
    print()
    print("Average total usage per dwelling (in 1000 gallons):")
    print(final)

    barplot = final.plot.bar(y="usagePerDwelling")
    plt.tight_layout()


# Call the main function so that
# this program will start executing.
main()
