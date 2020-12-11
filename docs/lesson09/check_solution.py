import pandas as pd

def main():
    try:
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("water.csv", parse_dates=["readDate"])

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
        filter = (df["accountType"] == "Residence")
        filtered_df = df[filter]
        print(filtered_df)

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


# If this file was executed like this:
# python check_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
