def main():
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        phone_numbers = []
        with open("phone_numbers.txt", "rt") as phone_file:
            for line in phone_file:
                phone_num = line.strip()
                phone_numbers.append(phone_num)

        # Print the list of phone numbers which will show that
        # some of the phone number don't have an area code.
        print(phone_numbers)

        # Some of the phone numbers in phone_numbers.txt do not start
        # with an area code. Replace each short phone number with a
        # phone number that begins with the area code "208-" To do this,
        # call the map function and pass the add_area_code function and
        # the list of phone numbers as arguments to the map function.
        pass

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
    pass


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

