import pandas as pd

def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("water.csv",
                dtype={"meterNumber":"str", "meterSize":"float32",
                    "readDate":"str", "numberOfDays":"int_", "usage":"int_",
                    "accountType":"str", "numberOfDwellings":"int_"
                },
                parse_dates=["readDate"])

        # Print the data type for each column in the data frame.
        print(df.dtypes)
        print()

        # Print a summary description of the data frame.
        print(df.describe())
        print()

        # Print the data frame.
        print(df)
        print()

        # Filter the data frame to residences
        # only and print the filtered data frame.
        filter = (data["accountType"] == "Residence")
        filtered_df = data[filter]
        print(filtered_df)

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


# Call the main function so that
# this program will start executing.
main()
