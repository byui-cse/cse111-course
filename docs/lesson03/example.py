import csv
import math
import datetime

# Create an empty dictionary that will
# store the data from the CSV file.
all_music = {}

# Open a file named all_music.csv and store a reference
# to the opened file in a variable named infile.
with open("all_music.csv", "rt") as infile:

    # Use the csv module to create a reader
    # object that will read from the opened file.
    reader = csv.reader(infile)

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

        # Store the data from the current row into the all_music
        # dictionary. Use the title as the key. Create a list
        # with the composer, album, and length as the value.
        all_music[title] = [composer, album, length]

# Print the entire music dictionary.
# print(all_music)
# print()

# Open a file named evening.txt and store a reference
# to the opened file in a variable named infile.
filename = "evening.txt"
with open(filename, "rt") as infile:

    # Read the entire evening.txt file into a large string.
    string = infile.read()

# Split the string into a list of strings. Each element in
# the list is one line of text from the evening.txt file.
playlist = string.splitlines()

# Print the entire playlist.
# print(playlist)
# print()

# Print the playlist name.
print(filename)

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
    value = all_music[title]
    length = value[2]
    print(title, length)
    total_length += length
print()

# Compute the total length of the playlist in minutes.
minutes = math.ceil(total_length / 60)

print(f"Total time: {minutes} minutes")
