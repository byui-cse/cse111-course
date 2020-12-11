"""
Write a Python program named fitness.py that does the following:
1. Reads the contents of the fitness.csv file.
2. Converts weight from pounds to kilograms (1 lb = 0.45359237 kg).
3. Converts inches to centimeters (1 in = 2.54 cm).
4. Calculates age, BMI, and BMR.
"""

import csv
import math
from datetime import date, datetime


def main():
    # Print headers for the six columns.
    print("Gender,Age (years),Weight (kg),Height (cm),BMI,BMR")

    # Open the CSV file fitness.csv for reading.
    with open("fitness.csv", "rt") as fitness:

        # Use the standard csv module to get
        # a reader object for the CSV file.
        reader = csv.reader(fitness)

        # The first line of the CSV file contains headings
        # and not fitness data, so this statement skips
        # the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # From the current row of the CSV file,
            # retrieve a person's gender from column 0.
            gender = row[0]

            # From the current row of the CSV file, retrieve a
            # person's birthdate as a string. Call the compute_age
            # function which convert the string to a date and then
            # compute and return a person's age in years.
            years = compute_age(row[1])

            # From the current row of the CSV file, retrieve a
            # person's weight in pounds and height in inches. Then
            # convert the person's weight from pounds to kilograms
            # and their height from inches to centimeters.
            pounds = float(row[2])
            inches = float(row[3])
            kg = round(kg_from_lb(pounds), 2)
            cm = round(cm_from_in(inches), 1)

            # For the current row, compute the person's
            # body mass index and basal metabolic rate.
            bmi = round(body_mass_index(kg, cm), 1)
            bmr = round(basal_metabolic_rate(gender, kg, cm, years), 1)

            # Display the results for the current row in the CSV file.
            print(gender, years, kg, cm, bmi, bmr, sep=",")


def compute_age(birth):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthdate = datetime.strptime(birth, "%Y-%m-%d").date()
    now = date.today()
    diff = now - birthdate
    years = math.floor(diff.days / 365.25)
    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = lb * 0.45359237
    return kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = inch * 2.54
    return cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()
