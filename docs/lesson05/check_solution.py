# Import necessary modules.
import csv


def main():
    # Open the CSV file fuel_usage.csv
    with open("fuel_usage.csv", "rt") as usage_file:

        # Use the standard csv module to get
        # a reader object for the CSV file.
        reader = csv.reader(usage_file)

        # The first line of the CSV file contains headings
        # and not fuel usage data, so this statement skips
        # the first line of the CSV file.
        next(reader)

        # Print headers for the three columns.
        print("Date,Miles/Gallon,Liters/100 Km")

        # Process each row in the CSV file.
        for row in reader:

            # From the current row of the CSV file, get the
            # date as a string. Don't bother to convert the
            # date from a string to a date object because the
            # only thing this program will do with the date is
            # print it, and a string works great for printing.
            date = row[0]

            # From the current row of the CSV file, get
            # starting and ending odometer readings.
            start = float(row[1])
            end = float(row[2])

            # From the current row of the CSV file, get
            # the number of gallons of fuel used.
            gallons = float(row[3])

            # Call the miles_per_gallon function.
            mpg = miles_per_gallon(start, end, gallons)

            # Call the lp100k_from_mpg function to convert the
            # miles per gallon to liters per 100 kilometers.
            lp100k = lp100k_from_mpg(mpg)

            # Display the results for one row in the csv file.
            print(date, round(mpg, 1), round(lp100k, 2), sep=",")


def miles_per_gallon(start, end, gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    start and end are odometer readings in miles.
    gallons is a fuel amount in U.S. gallons.
    """
    mpg = abs(end - start) / gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    """
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()
