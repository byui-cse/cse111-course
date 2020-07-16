import csv


def main():
    # Print headers for the three columns.
    print("Date,Miles/Gallon,Liters/100 Km")

    # Open the CSV file fuel_usage.csv
    with open("fuel_usage.csv", "rt") as fuel:

        # Use the standard csv module to get
        # a reader object for the CSV file.
        reader = csv.reader(fuel)

        # Process each row in the CSV file.
        for row in reader:

            # The first line of the CSV file contains headings
            # and not fuel usage data, so this if statement
            # will skip the first line of the CSV file.
            if reader.line_num > 1:

                # Get the date as a string from the csv file. Don't
                # bother to convert the date from a string to a date
                # object because the only thing this program will do
                # with the date is print it, and a string works great
                # for printing.
                date = row[0]

                # Get starting and ending odometer
                # readings from the csv file.
                start = float(row[1])
                end = float(row[2])

                # Get the number of gallons of
                # fuel used from the csv file.
                gallons = float(row[3])

                # Call the miles_per_gallon function.
                mpg = miles_per_gallon(start, end, gallons)

                # Call the lp100k_from_mpg function to convert the
                # miles per gallon to liters per 100 kilometers.
                lp100k = lp100k_from_mpg(mpg)

                # Display the results for one row in the csv file.
                print(date, round(mpg, 1), round(lp100k, 2), sep=",")


def miles_per_gallon(start, end, gallons):
    """Compute and return the average miles that
    a vehicle traveled per gallon of fuel."""
    mpg = abs(end - start) / gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100 kilometers."""
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()
