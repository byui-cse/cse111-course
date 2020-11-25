import pandas as pd


def main():
    try:
        # Read the students.csv file and convert the
        # birthdate column from a string to a datetime64.
        df = pd.read_csv("students.csv", parse_dates=["birthdate"])

        # Some of the phone numbers in the "phone" column do not start
        # with an area code, so replace the "phone" column with a new
        # "phone" column where every phone number starts with an area
        # code. To do this, call the pandas apply function for the
        # "phone" column and pass the add_area_code function as an
        # argument to the apply function.
        df["phone"] = df["phone"].apply(add_area_code)

        # Print the DataFrame with the corrected phone numbers.
        print(df)

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def add_area_code(phone):
    """Phone numbers in the U.S. are often stored as ten digits and two
    dashes in this format: "ddd-ddd-dddd" where each d is a digit. If
    the length of the phone parameter is less than 12 characters, add
    the area code "208-" at the beginning of the phone number and return
    the phone number.

    param phone: a string of digits formatted as "ddd-dddd" or "ddd-ddd-dddd"
    return: a string of digits formated as "ddd-ddd-dddd"
    """
    if len(phone) < 12:
        phone = "208-" + phone
    return phone


# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()
