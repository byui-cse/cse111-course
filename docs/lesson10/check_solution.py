import pandas as pd
import matplotlib.pyplot as pyplot


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("../lesson09/water.csv", parse_dates=["readDate"])
        #print(df)

        # Convert the readDate column from a datetime64 to just a date
        # so that the plot will not contain an empty time of "00:00:00"
        # for each date.
        df["readDate"] = df["readDate"].dt.date
        #print(df)

        # Filter the data frame to readings for meter #M4103 only.
        meternum = "M4103"
        filter = (df["meterNumber"] == meternum)
        m4103_df = df[filter]
        #print(m4103_df)

        # Define a vertical bar plot from the data frame for meter #M4103.
        m4103_df.plot(kind="bar", x="readDate", y="usage",
                title=f"Water Usage for Meter #{meternum}",
                color="lightseagreen",
                xlabel="", ylabel="x1000 gallons", legend=None)

        # Call the pyplot.tight_layout() function, which will format the
        # previously defined plot so that all of its parts are spaced
        # nicely. Strangely, pyplot.tight_layout() must be called
        # multiple times, once for each defined plot, but pyplot.show()
        # needs to be called only once.
        pyplot.tight_layout()

        # Show all defined plots.
        pyplot.show()

    except RuntimeError as run_err:
        # Print information about the runtime error.
        print(type(run_err).__name__, run_err, sep=": ")


# If this file is executed like this:
# > python check_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
