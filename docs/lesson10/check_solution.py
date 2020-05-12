import matplotlib.pyplot as plt
import pandas as pd


def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("../lesson09/water.csv",
            dtype={"meterNumber":"str",
                "readDate":"str", "numberOfDays":"int_",
                "reading":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])

    # Convert the readDate column from a datetime64 to just a date.
    data["readDate"] = data["readDate"].dt.date

    # Filter the data to meter #M4103 only.
    metnum = "M4103"
    m4103 = data[data["meterNumber"] == metnum]

    # Define a vertical bar plot from the data for meter #M4103.
    barplot = m4103.plot.bar(x="readDate", y="usage", legend=False)
    barplot.set_title(f"Water Usage for Meter #{metnum}")
    barplot.set_xlabel("")
    barplot.set_ylabel("x1000 gallons")
    plt.tight_layout()

    # Show all defined plots.
    plt.show()


main()
