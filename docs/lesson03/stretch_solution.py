# Copyright 2025, Brigham Young University-Idaho. All rights reserved.

"""
Write a Python program named fitness.py that does the following:
1. Asks the user to enter four values:
    a. gender
    b. birthdate in this format: YYYY-MM-DD
    c. weight in U.S. pounds
    d. height in U.S. inches
2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg)
3. Converts inches to centimeters (1 in = 2.54 cm).
4. Calculates age, BMI, and BMR.
5. Prints age, weight in kg, height in cm, BMI, and BMR.
"""

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")

    # Call the get_weight_kg function to
    # get the user's weight in kilograms.
    kg = get_weight_kg()

    # Call the get_height_cm function to
    # get the user's height in centimeters.
    cm = get_height_cm()

    # Call the body_mass_index function.
    bmi = body_mass_index(kg, cm)

    # Call the basal_metabolic_rate function.
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    # Print the results for the user to see.
    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")

    # Compute the difference between today and the
    # person's birthdate in years.
    today = datetime.now()
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def get_weight_kg():
    """Get the user's weight and convert and return it in kilograms."""

    print()
    print("Please choose one of the following units to enter your weight:")
    print("[K]ilograms")
    print("U.S. [P]ounds")
    print("British [S]tones")
    units = input("Which units do you want to use to enter your weight (K, P, or S)? ")
    choice = units.upper()[0]
    if choice == 'K':
        kg = float(input("Enter your weight in kilograms: "))
    elif choice == 'P':
        pounds = float(input("Enter your weight in U.S. pounds: "))
        kg = kg_from_lb(pounds)
    elif choice == 'S':
        stones = float(input("Etner your weight in British stones: "))
        kg = kg_from_stone(stones)
    else:
        print(f"Error: invalid weight units {units}")
    return kg


def kg_from_lb(pounds):
    """Convert a mass in U.S. pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237
    return kg


def kg_from_stone(stones):
    """Convert a mass in British stones to kilograms.
    Parameter stones: a mass in British stones.
    Return: the mass in kilograms.
    """
    kg = stones * 6.35029
    return kg


def get_height_cm():
    """Get the user's height and convert and return it in centimeters."""

    print()
    print("Please choose one of the following units to enter your height:")
    print("[M]eters")
    print("[C]entimeters")
    print("U.S. [I]nches")
    print("U.S. [F]eet and inches")
    units = input("Which units do you want to use to enter your height (M, C, I, or F)? ")
    choice = units.upper()[0]
    if choice == 'M':
        m = float(input("Enter your height in meters: "))
        cm = cm_from_m(m)
    elif choice == 'C':
        cm = float(input("Enter your height in centimeters: "))
    elif choice == 'I':
        inches = float(input("Enter your height in U.S. inches: "))
        cm = cm_from_in(inches)
    elif choice == 'F':
        text = input("Enter your height in U.S. feet and inches (ex. 5 10): ")
        parts = text.split()
        feet = int(parts[0])
        inches = float(parts[1])
        cm = cm_from_in(feet * 12 + inches)
    else:
        print(f"Error: invalid height units {units}")
    return cm


def cm_from_m(meters):
    """Convert a length in meters to centimeters.
    Parameter meters: a length in meters.
    Return: the length in centimeters.
    """
    cm = meters * 100
    return cm


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()
