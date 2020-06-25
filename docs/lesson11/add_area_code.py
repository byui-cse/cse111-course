import pandas as pd


def main():
    # Read the students.csv file and convert the
    # birthdate column from a string to a datetime64.
    df = pd.read_csv("students.csv", parse_dates=["birthdate"])

    # Call the pandas apply function for the "phone" column and
    # pass the add_area_code function as an argument to the apply
    # function. The apply function will call the add_area_code
    # function once for each phone number in the "phone" column,
    # and the add_area_code function will add Idaho's area code
    # "208-" at the beginning of the phone number if necessary.
    df["phone"] = df["phone"].apply(add_area_code)

    # Write the data frame with the corrected phone
    # numbers to a new CSV file named students2.csv.
    df.to_csv("students2.csv", mode="wt", line_terminator="\n")


def add_area_code(phone):
    """Phone numbers in the U.S. are usually stored as ten digits and
    two dashes in this format: "ddd-ddd-dddd" where each d is a digit.
    If the length of the phone parameter is less than 12 characters, add
    the area code "208-" at the beginning of the phone number. Return
    the phone number.
    """
    pass


# Call the main function so that
# this program will start executing.
main()
