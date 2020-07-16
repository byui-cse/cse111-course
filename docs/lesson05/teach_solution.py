import csv
import math
from datetime import date, datetime


def main():
    print("Gender,Age (years),Weight (kg),Height (cm),BMI,BMR")
    with open("fitness.csv", "rt") as fitness:
        reader = csv.reader(fitness)
        for row in reader:

            # The first line of the CSV file contains headings
            # and not fitness data, so this if statement
            # will skip the first line of the CSV file.
            if reader.line_num > 1:

                # From the current row, retrieve a
                # person's gender from column 0.
                gender = row[0]

                # From the current row, retrieve a person's birthdate
                # as a string. Call the compute_age function which
                # convert the string to a date and then compute and
                # return a person's age in years.
                years = compute_age(row[1])

                # From the current row, retrieve a person's weight
                # in pounds and height in inches. Then convert the
                # person's weight from pounds to kilograms and their
                # height from inches to centimeters.
                pounds = float(row[2])
                inches = float(row[3])
                kg = round(kg_from_lb(pounds), 2)
                cm = round(cm_from_in(inches), 1)

                # For the current row, compute the person's
                # body mass index and basal metabolic rate.
                bmi = round(body_mass_index(kg, cm), 1)
                bmr = round(basal_metabolic_rate(gender, kg, cm, years), 1)

                # Display the results for the
                # current row in the CSV file.
                print(gender, years, kg, cm, bmi, bmr, sep=",")


def compute_age(birth):
    """Compute and return a person's age in years.

    param birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    """
    birthdate = datetime.strptime(birth, "%Y-%m-%d").date()
    now = date.today()
    diff = now - birthdate
    years = math.floor(diff.days / 365.25)
    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms."""
    kg = lb * 0.45359237
    return kg

def cm_from_in(inch):
    """Convert a length in inches to centimeters."""
    cm = inch * 2.54
    return cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass
    index (bmi). weight and height must be in
    kilograms and centimeters, respectively.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic
    rate (bmr). weight must be in kilograms, height
    must be in centimeters, and age must be in years.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()
