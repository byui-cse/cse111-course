import csv
import math

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
print(all_music)
print()

with open("evening.txt", "rt") as infile:
    string = infile.read()
playlist = string.splitlines()
print(playlist)
print()

total_length = 0
for title in playlist:
    value = all_music[title]
    length = value[2]
    print(title, length)
    total_length += length
print()

minutes = math.ceil(total_length / 60)
print(f"Total time: {minutes} minutes")
