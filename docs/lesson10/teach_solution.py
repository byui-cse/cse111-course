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


