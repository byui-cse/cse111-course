import pandas as pd


def main():
    try:
        # Read the students.csv file and convert the
        # birthdate column from a string to a datetime64.
        original_df = pd.read_csv("students.csv", parse_dates=["birthdate"])

        # Print the DataFrame which will show that some
        # of the phone numbers don't have area codes.
        print(original_df)

        # Some of the phone numbers in the "phone" column do not start
        # with an area code, so replace the "phone" column with a new
        # "phone" column where every phone number starts with an area
        # code. To do this, call the pandas apply function for the
        # "phone" column and pass the add_area_code function as an
        # argument to the apply function.
        pass

        # Print the DataFrame with the corrected phone numbers.
        print(original_df)

    except RuntimeError as run_err:
        print(type(run_err).__name__, run_err, sep=": ")


def add_area_code(phone):
    """Phone numbers in the U.S. are often stored as ten digits and two
    dashes in this format: "ddd-ddd-dddd" where each d is a digit. If
    the length of the phone parameter is less than 12 characters, add
    the area code "208-" at the beginning of the phone number and return
    the phone number.

    param phone: a string of digits formatted as "ddd-dddd" or "ddd-ddd-dddd"
    return: a string of digits formated as "ddd-ddd-dddd"
    """
    pass


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
