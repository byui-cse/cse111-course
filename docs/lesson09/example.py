import csv
import math
import datetime


def main():
    music_dict = read_music_data("all_music.csv")
    process_playlist("evening.txt", music_dict)


def read_music_data(filename):
    # Create an empty dictionary that will
    # store the data from the CSV file.
    music_dict = {}

    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named music_file.
    with open(filename, "rt") as music_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(music_file)

        # The first line of the CSV file contains column headings
        # and not information about a dental office, so this
        # statement skips the first line of the CSV file.
        next(reader)

        # Read each row one at a time as a list.
        for row in reader:

            # For the current row, retrieve the
            # values in columns 0 through 4.
            title = row[0]
            composer = row[1]
            album = row[2]
            year = int(row[3])
            length = int(row[4])

            # Store the data from the current row into the music_dict
            # dictionary. Use the title as the key. Create a list
            # with the composer, album, and length as the value.
            music_dict[title] = [composer, album, length]

    # Print the entire music dictionary.
    # print(music_dict)
    # print()

    return music_dict


def process_playlist(filename, music_dict):
    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named play_file.
    with open(filename, "rt") as play_file:

        # Read the entire evening.txt file into a large string.
        string = play_file.read()

    # Split the string into a list of strings. Each element in
    # the list is one line of text from the evening.txt file.
    playlist = string.splitlines()

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
        length = value[2]
        print(title, length)
        total_length += length
    print()

    # Compute the total length of the playlist in minutes.
    minutes = math.ceil(total_length / 60)

    print(f"Total time: {minutes} minutes")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
