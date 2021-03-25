import csv
import math
import datetime


def main():
    # The headings and indexes of the columns in the all_music.csv file.
    TITLE = 0
    COMPOSER = 1
    ALBUM = 2
    YEAR = 3
    LENGTH = 4

    # Read the information about all music
    # into a dictionary named music_dict.
    music_dict = read_dict("all_music.csv", TITLE)

    # Read the list of music in the evening.txt
    # file into a list named playlist.
    filename = "evening.txt"
    playlist = read_list(filename)

    # Print the playlist name.
    print(filename)

    # Print the entire playlist.
    # print(playlist)
    # print()

    # Get the current date and time from the datetime
    # module which gets it from the operating system.
    current_date_and_time = datetime.datetime.now()

    # Format the current date and time to include only
    # the day of the week, the hour, and the minute.
    string = current_date_and_time.strftime("%Y %B %d")

    # Print the formatted string.
    print(string)
    print()

    # Sum the total length of the playlist in seconds.
    total_length = 0
    for title in playlist:
        value = music_dict[title]
        length = int(value[LENGTH])
        print(title, length)
        total_length += length
    print()

    # Compute the total length of the playlist in minutes.
    minutes = math.ceil(total_length / 60)

    print(f"Total time: {minutes} minutes")


def read_dict(filename, key_column_index):
    """Read the contens of a CSV file into a dictionary
    and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(text_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row

    # Return the dictionary.
    return dictionary


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
