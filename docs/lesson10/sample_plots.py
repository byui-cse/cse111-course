import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
import pandas as pd


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("../lesson09/water.csv", parse_dates=["readDate"])

        combine_account_types(df)
        sum_df = sum_usage_by_account_type(df)

        # Call the show_usage_sum function which will define two plots.
        show_usage_sum(sum_df)

        # Show all defined plots.
        pyplot.show()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def combine_account_types(df):
    """The water.csv file contains too many account types to be
    shown neatly in a pie plot, so combine some of the account types.
    """
    categories = {
        "Airport Hanger" : "Other",
        "Apartment Complex" : "Apt. Complex",
        "Business" : "Business",
        "Business with Apartment" : "Business",
        "BYU-Idaho" : "BYU-Idaho",
        "Church" : "Church",
        "City" : "City",
        "Free" : "Other",
        "Out of Town" : "Out of Town",
        "Residence" : "Residence",
        "Residence with Apartment" : "Residence",
        "School" : "School",
        "Sprinklers" : "Other",
        "Town Homes" : "Town Homes",
        "Trailer Court" : "Trailer Court",
        "Vacant" : "Other",
    }

    # Use the Pandas DataFrame.map function
    # to combine some of the account types.
    df["accountType"] = df["accountType"].map(categories)


def sum_usage_by_account_type(df):
    """Create and return a new data frame that
    contains total water usage by account type.
    """
    group = df.groupby("accountType")
    sum_df = group.aggregate(sumUsage=("usage", "sum")).reset_index()
    return sum_df


def show_usage_sum(sum_df):
    """Define a pie plot and a vertical bar plot
    that both show total water usage by account type.
    """
    colors = {
        "City":"gold", "School":"purple", "BYU-Idaho":"violet",
        "Apt. Complex":"pink",
        "Trailer Court":"green", "Town Homes":"lime",
        "Out of Town":"gray",
        "Residence":"yellow",
        "Business":"skyblue",
        "Other":"brown", "Church":"orange",
    }

    # Create a dictionary that contains the
    # desired order for the account types.
    order = colors.keys()
    order = dict(zip(order, range(len(order))))

    # Get the colors that will be used in both plots.
    colors = colors.values()

    # Add a column named order that contains the desired sort order.
    sum_df["order"] = sum_df["accountType"].map(order)

    # Sort the data by the values in the "order" column.
    sum_df.sort_values("order", inplace=True)

    # Keep only the accountType and usage columns.
    columns = ["accountType", "sumUsage"]
    sum_df = sum_df[columns]

    # Make the accountType column be the index.
    sum_df.set_index("accountType", inplace=True)

    # Print the data frame so we can verify that it's correct.
    print(sum_df)

    # Define a pie plot.
    title = "Water Usage 2015 - 2019"
    sum_df.plot(kind="pie", y="sumUsage", colors=colors,
            title=title, label="", legend=None)

    # Call the pyplot.tight_layout function, which will format the
    # previously defined plot so that all of its parts are spaced
    # nicely. Strangely, pyplot.tight_layout must be called multiple
    # times, once for each defined plot, but pyplot.show needs to be
    # called only once.
    pyplot.tight_layout()

    # Define a vertical bar plot.
    bar = sum_df.plot(kind="bar", y="sumUsage", color=colors,
            title=title, legend=None)
    bar.set_xlabel("")
    bar.set_ylabel("x1000 gallons")
    fmtr = ticker.FuncFormatter(lambda val, pos: f"{val:,.0f}")
    bar.yaxis.set_major_formatter(fmtr)

    # Call the pyplot.tight_layout function, which will format the
    # previously defined plot so that all of its parts are spaced
    # nicely. Strangely, pyplot.tight_layout must be called multiple
    # times, once for each defined plot, but pyplot.show needs to be
    # called only once.
    pyplot.tight_layout()


# Call the main function so that
# this program will start executing.
main()
