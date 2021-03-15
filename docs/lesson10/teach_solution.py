import pandas as pd
import matplotlib.pyplot as pyplot


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        original_df = pd.read_csv("../lesson09/water.csv", parse_dates=["readDate"])

        # Add to the original data frame a year column
        # that contains the year from each readDate.
        original_df["year"] = original_df["readDate"].dt.year

        show_all_water_usage(original_df)

        show_water_usage_for_account_type(original_df, "Apartment Complex", "pink")
        show_water_usage_for_account_type(original_df, "Business", "skyblue")

        show_water_usage_per_dwelling(original_df)

        # Show all defined plots.
        pyplot.show()

    except RuntimeError as run_err:
        print(type(run_err).__name__, run_err, sep=": ")


def show_all_water_usage(df):
    # For each year, compute the total water usage.
    group = df.groupby("year")
    total_df = group.aggregate(sumUsage=("usage", "sum"))

    print()
    print("Total water usage by year (in 1000 gallons):")
    print(total_df)

    barplot = total_df.plot(kind="bar", y="sumUsage",
            title="Total Water Usage by Year",
            xlabel="", ylabel="x1000 gallons", legend=None)

    # Call the pyplot.tight_layout function, which will format the
    # previously defined plot so that all of its parts are spaced
    # nicely. Strangely, pyplot.tight_layout must be called multiple
    # times, once for each defined plot, but pyplot.show needs to be
    # called only once.
    pyplot.tight_layout()


def show_water_usage_for_account_type(df, account_type, color):
    # Filter the data frame to the given account type.
    filter = (df["accountType"] == account_type)
    type_df = df[filter]

    # For each year, compute the total water usage.
    group = type_df.groupby("year")
    total_df = group.aggregate(sumUsage=("usage", "sum"))

    print()
    print(f"{account_type} water usage by year (in 1000 gallons):")
    print(total_df)

    barplot = total_df.plot(kind="bar", y="sumUsage", color=color,
            title=f"{account_type} Water Usage by Year",
            xlabel="", ylabel="x1000 gallons", legend=None)

    # Call the pyplot.tight_layout function, which will format the
    # previously defined plot so that all of its parts are spaced
    # nicely. Strangely, pyplot.tight_layout must be called multiple
    # times, once for each defined plot, but pyplot.show needs to be
    # called only once.
    pyplot.tight_layout()


def show_water_usage_per_dwelling(df):
    # Filter the data frame to apartment complexes,
    # residences, trailer courts, and town homes only.
    filter = (df["accountType"] == "Apartment Complex") | \
            (df["accountType"] == "Residence") | \
            (df["accountType"] == "Trailer Court") | \
            (df["accountType"] == "Town Homes")
    housing_df = df[filter]

    # For each meterNumber, compute the total water
    # usage and the number of dwellings grouped by year.
    group = housing_df.groupby(["meterNumber", "year"])
    interm_df = group.aggregate(usage=("usage", "sum"),
            numberOfDwellings=("numberOfDwellings", "mean"))

    # Discard outliers: rows with numDwellings less than 1.
    filter = (interm_df["numberOfDwellings"] >= 1)
    normal_df = interm_df[filter]

    # For each year, compute the total water
    # usage and the total number of dwellings.
    group = normal_df.groupby("year")
    final_df = group.aggregate(sumUsage=("usage", "sum"),
            sumDwellings=("numberOfDwellings", "sum"))

    # Add a computed column that is sumUsage / numDwellings.
    final_df["usagePerDwelling"] = final_df["sumUsage"] / final_df["sumDwellings"]

    pd.options.display.float_format = "{:.1f}".format
    print()
    print("Average usage per dwelling (in 1000 gallons):")
    print(final_df)

    barplot = final_df.plot(kind="bar", y="usagePerDwelling", color="lime",
            title="Average Usage per Dwelling",
            xlabel="", ylabel="x1000 gallons", legend=None)

    # Call the pyplot.tight_layout function, which will format the
    # previously defined plot so that all of its parts are spaced
    # nicely. Strangely, pyplot.tight_layout must be called multiple
    # times, once for each defined plot, but pyplot.show needs to be
    # called only once.
    pyplot.tight_layout()


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
