def main():
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        phone_numbers = read_list("phone_numbers.txt")

        # Print the list of phone numbers which will show that
        # some of the phone number don't have an area code.
        print(phone_numbers)

        # Some of the phone numbers in phone_numbers.txt do not start
        # with an area code. Replace each short phone number with a
        # phone number that begins with the area code "208-" To do this,
        # call the map function and pass the add_area_code function and
        # the list of phone numbers as arguments to the map function.
        new_numbers = list(map(add_area_code, phone_numbers))

        # Print the list with the corrected phone numbers.
        print(new_numbers)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def add_area_code(phone_number):
    """Phone numbers in the U.S. are often stored as ten digits and
    two dashes in this format: "ddd-ddd-dddd" where each d is a digit.
    If the length of phone_number is less than 12 characters, add the
    area code "208-" at the beginning of the phone_number and return
    phone_number.

    Parameter phone_number: a string of digits formatted as
        "ddd-dddd" or "ddd-ddd-dddd"
    Return: a string of digits formated as "ddd-ddd-dddd"
    """
    if len(phone_number) < 12:
        phone_number = "208-" + phone_number
    return phone_number


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# If this file is executed like this:
# > python check_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
