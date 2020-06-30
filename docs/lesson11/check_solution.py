import pandas as pd


def main():
    # Read the students.csv file and convert the
    # birthdate column from a string to a datetime64.
    df = pd.read_csv("students.csv", parse_dates=["birthdate"])

    # Some of the phone numbers in the "phone" column do not
    # start with the area code, so replace the "phone" column
    # with a new "phone" column where every phone number starts
    # with an area code. To do this, call the pandas apply
    # function for the "phone" column and pass the add_area_code
    # function as an argument to the apply function.
    df["phone"] = df["phone"].apply(add_area_code)

    # Write the data frame with the corrected phone
    # numbers to a new CSV file named students2.csv.
    df.to_csv("students2.csv", mode="wt", index=False, line_terminator="\n")


def add_area_code(phone):
    """Phone numbers in the U.S. are often stored as ten digits
    and two dashes in this format: "ddd-ddd-dddd" where each d
    is a digit. If the length of the phone parameter is less
    than 12 characters, add the area code "208-" at the
    beginning of the phone number. Return the phone number.
    """
    if len(phone) < 12:
        phone = "208-" + phone
    return phone


# Call the main function so that
# this program will start executing.
main()
