import pandas as pd

def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("water.csv",
            dtype={"meterNumber":"str", "meterSize":"float32",
                "readDate":"str", "numberOfDays":"int_", "usage":"int_",
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

    # Filter the data to residences only and print the filtered data.
    filtered = data[data["accountType"] == "Residence"]
    print(filtered)


# Call the main function so that
# this program will start executing.
main()
