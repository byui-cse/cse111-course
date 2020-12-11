import pandas as pd
import matplotlib.pyplot as pyplot


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("../lesson09/water.csv", parse_dates=["readDate"])

        # Convert the readDate column from a datetime64 to just a date.
        df["readDate"] = df["readDate"].dt.date

        # Filter the data frame to readings for meter #M4103 only.
        meternum = "M4103"
        filter = (df["meterNumber"] == meternum)
        m4103_df = df[filter]

        # Define a vertical bar plot from the data frame for meter #M4103.
        barplot = m4103_df.plot(kind="bar", x="readDate", y="usage",
                title=f"Water Usage for Meter #{meternum}", legend=None)
        barplot.set_xlabel("")
        barplot.set_ylabel("x1000 gallons")

        # Call the pyplot.tight_layout function, which will format the
        # previously defined plot so that all of its parts are spaced
        # nicely. Strangely, pyplot.tight_layout must be called multiple
        # times, once for each defined plot, but pyplot.show needs to be
        # called only once.
        pyplot.tight_layout()

        # Show all defined plots.
        pyplot.show()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


# If this file was executed like this:
# python check_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
