"""
Write a Python program named provinces.py that reads the contents
of provinces.txt into a list and then modifies the list.
"""

def main():
    # Create an empty list that will hold all of the provinces.
    provinces = []

    # Open the provinces.txt text file for reading.
    with open("provinces.txt", "rt") as infile:

        # Read all the lines of the file into a list
        # named provinces. Each line of the file will
        # be stored in its own element in the list.
        for line in infile:

            # Strip all white space that surrounds the
            # text on the line, including the newline
            # character at the end of the line.
            clean_line = line.strip()

            # Append the line of text onto the provinces list.
            provinces.append(clean_line)

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


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
