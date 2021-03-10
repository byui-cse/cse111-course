import csv


# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        # Prompt the user for a filename and open that text file.
        infile = None
        while infile == None:
            filename = input("Name of file that contains NHTSA data: ")
            try:
                infile = open(filename, "rt")
            except (FileNotFoundError, PermissionError) as error:
                print(error)
                print("Please choose a different file.")
        print()

        # Prompt the user for a percentage.
        perc_reduc = None
        while perc_reduc == None:
            try:
                perc_reduc = float(input("Percent reduction of texting while driving [0, 100]: "))
                if perc_reduc < 0:
                    print(f"Error: {perc_reduc} is too low.",
                            "Please enter a different number.", sep="\n")
                    perc_reduc = None
                elif perc_reduc > 100:
                    print(f"Error: {perc_reduc} is too high.",
                            "Please enter a different number.", sep="\n")
                    perc_reduc = None
            except ValueError as val_err:
                print("Error:", val_err)
        print()

        print(f"With a {perc_reduc}% reduction in using a cell phone while",
                "driving, approximately this number of injuries and",
                "deaths would have been prevented in the USA.", sep="\n")
        print()
        print("Year, Injuries, Deaths")

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(infile)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:
            year = row[YEAR_COLUMN]

            # Call the estimate_reduction function.
            injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)

            # Print the estimated reductions in injuries and fatalities.
            print(year, injur, fatal, sep=", ")

    except (csv.Error, KeyError) as error:
        print(f"Error: line {reader.line_num} of {infile.name} is"
                " formatted incorrectly.")
    except ZeroDivisionError as zero_div_err:
        print(f"Error: line {reader.line_num} of {infile.name} contains"
                " 0 in the 'Fatal Crashes' or 'Cell Phone Use' column.")
    except RuntimeError as run_err:
        # RuntimeError is probably the most general type of exception
        # that you want to handle in a Python program. Exception is
        # more general than RuntimeError. However, Exception includes
        # SyntaxError, and you probably don't want to handle
        # SyntaxError. Instead, you want your program to crash for
        # SyntaxError and print the line number where the SyntaxError
        # occurred.
        print(type(run_err).__name__, run_err, sep=": ")
    finally:
        if infile is not None:
            # Close the text file.
            infile.close()


def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that would
    not have occurred on U.S. roads and highways if drivers had reduced
    a dangerous behavior by a given percentage.

    Params:
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


# Call the main function so that
# this program will start executing.
main()
