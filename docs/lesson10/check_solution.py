import matplotlib.pyplot as plot
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
    data["year"] = data["readDate"].dt.year

    first = data[["accountType", "usage"]]
    first = first.groupby("accountType").aggregate(sumUsage=("usage", "sum"))
    first.plot()

    second = data[["year", "usage"]]
    second = second.groupby("year").aggregate(sumUsage=("usage", "sum"))
    second.plot()

    third = data[["meterNumber", "usage", "accountType"]]
    third = third[third["accountType"]
                .isin(["Business", "Business with Apartment"])]
    third = third.groupby("meterNumber").aggregate(sumUsage=("usage", "sum"))
    third.plot()

    plot.show()


main()
