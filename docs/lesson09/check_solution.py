"""
Write a Python program named provinces.py that reads the contents
of provinces.txt into a list and then modifies the list.
"""

def main():
    # Read the contents of a text file named
    # provinces.txt into a list named provinces.
    provinces = read_list("provinces.txt")

    # As a debugging aid, print the entire list.
    print(provinces)

    # Remove the first element from the list.
    provinces.pop(0)
    #print(provinces)

    # Remove the last element from the list.
    provinces.pop()
    #print(provinces)

    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"
    #print(provinces)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_lines.
    text_lines = []

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
            text_lines.append(clean_line)

    # Return the list that contains the lines of text.
    return text_lines


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
