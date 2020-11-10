import pandas as pd
import matplotlib.pyplot as plt


def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("../lesson09/water.csv",
                dtype={"meterNumber":"str", "meterSize":"float32",
                    "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                    "accountType":"str", "numberOfDwellings":"int_"
                },
                parse_dates=["readDate"])

        # Convert the readDate column from a datetime64 to just a date.
        df["readDate"] = df["readDate"].dt.date

        # Filter the data frame to readings for meter #M4103 only.
        meternum = "M4103"
        filter = df["meterNumber"] == meternum
        m4103_df = df[filter]

        # Define a vertical bar plot from the data frame for meter #M4103.
        barplot = m4103_df.plot.bar(x="readDate", y="usage", legend=False)
        barplot.set_title(f"Water Usage for Meter #{meternum}")
        barplot.set_xlabel("")
        barplot.set_ylabel("x1000 gallons")
        plt.tight_layout()

        # Show all defined plots.
        plt.show()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


# Call the main function so that
# this program will start executing.
main()
