import pandas as pd

def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("water.csv",
            dtype={"meterNumber":"str",
                "readDate":"str", "numberOfDays":"int_",
                "reading":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])

    # Print the data type for each column.
    print(data.dtypes)
    print()

    # Print a summary description of the data.
    print(data.describe())
    print()

    # Print the data.
    print(data)
    print()

    # Filter the data to residences only.
    filtered = data[data["accountType"] == "Residence"]
    print(filtered)


main()
