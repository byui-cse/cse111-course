import pandas as pd
import matplotlib.pyplot as pyplot


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("../lesson09/water.csv", parse_dates=["readDate"])

        # Add to the DataFrame a year column that
        # contains the year from each readDate.
        df["year"] = df["readDate"].dt.year

        show_all_water_usage(df)

        show_water_usage_per_dwelling(df)

        # Show all defined plots.
        pyplot.show()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def show_all_water_usage(df):
    # For each year, compute the total water usage.
    group = df.groupby("year")
    total_df = group.aggregate(sumUsage=("usage", "sum"))

    print()
    print("Total water usage by year (in 1000 gallons):")
    print(total_df)

    barplot = total_df.plot.bar(y="sumUsage",
            title="Total Water Usage by Year", legend=None)
    barplot.set_xlabel("")
    barplot.set_ylabel("x1000 gallons")
    pyplot.tight_layout()


def show_water_usage_per_dwelling(df):
    # Filter the data frame to apartment complexes,
    # residences, trailer courts, and town homes only.
    filter = (df["accountType"] == "Apartment Complex") | \
            (df["accountType"] == "Residence") | \
            (df["accountType"] == "Trailer Court") | \
            (df["accountType"] == "Town Homes")
    df = df[filter]

    # For each meterNumber, compute the total water
    # usage and the number of dwellings grouped by year.
    group = df.groupby(["meterNumber", "year"])
    interm_df = group.aggregate(usage=("usage", "sum"),
            numberOfDwellings=("numberOfDwellings", "mean"))

    # Discard outliers: rows with numDwellings less than 1.
    filter = (interm_df["numberOfDwellings"] >= 1)
    interm_df = interm_df[filter]

    # For each year, compute the total water
    # usage and the total number of dwellings.
    group = interm_df.groupby("year")
    final_df = group.aggregate(sumUsage=("usage", "sum"),
            sumDwellings=("numberOfDwellings", "sum"))

    # Add a computed column that is sumUsage / numDwellings.
    final_df["usagePerDwelling"] = final_df["sumUsage"] / final_df["sumDwellings"]

    pd.options.display.float_format = "{:.1f}".format
    print()
    print("Average usage per dwelling (in 1000 gallons):")
    print(final_df)

    barplot = final_df.plot.bar(y="usagePerDwelling",
            title="Average Usage per Dwelling", legend=None)
    barplot.set_xlabel("")
    barplot.set_ylabel("x1000 gallons")
    pyplot.tight_layout()


# Call the main function so that
# this program will start executing.
main()
