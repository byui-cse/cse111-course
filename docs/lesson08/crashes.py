import csv


YEAR_KEY = "Year"
FATALITIES_KEY = "Fatalities"
INJURIES_KEY = "Injuries"
CRASHES_KEY = "Crashes"
FATAL_CRASHES_KEY = "Fatal Crashes"
DISTRACTION_KEY = "Distraction Affected Fatal Crashes"
PHONE_KEY = "Fatal Crashes involving Cell Phone Use"
SPEED_KEY = "Fatal Crashes involving Excessive Speed"
DUI_KEY = "Fatal Crashes while Driving under the Influence"
FATIGUE_KEY = "Fatal Crashes involving Fatigue or Illness"


def main():
    # Prompt the user for a filename and open that text file.
    filename = input("Name of file that contains NHTSA data: ")
    infile = open(filename, "rt")
    print()

    # Prompt the user for a percentage.
    perc_reduc = float(input("Percent reduction of texting while driving: "))
    print()

    print(f"With a {perc_reduc}% reduction in using a cell phone while\n"+
        "driving, approximately this number of injuries and\n" +
        "deaths would have been prevented in the USA.")
    print()

    # Process each row in the CSV file.
    print("Year, Injuries, Deaths")
    reader = csv.DictReader(infile)
    for row in reader:
        year = row[YEAR_KEY]
        injur, fatal = estimate_reduction(row, PHONE_KEY, perc_reduc)
        print(year, injur, fatal, sep=", ")

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
    fatal_crashes = int(row[FATAL_CRASHES_KEY])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_KEY])
    injuries = int(row[INJURIES_KEY])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


main()
