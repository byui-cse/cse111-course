"""
Write a Python program named fitness.py that does the following:
1. Asks the user to enter four values:
    a. gender
    b. birthdate in this format: YYYY-MM-DD
    c. weight in US pounds
    d. height in US inches
2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
3. Converts inches to centimeters (1 in = 2.54 cm).
4. Calculates age, BMI, and BMR.
5. Prints age, weight in kg, height in cm, BMI, and BMR.
"""

# Import datetime so that it can be
# used to compute a person's age.
import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Please enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in US pounds: "))
    inches = float(input("Enter your height in US inches: "))

    # Call the compute_age function.
    years = compute_age(birthdate)

    # Call the kg_from_lb function to convert from pounds to kilograms
    # and then round the result to two digits after the decimal.
    kg = round(kg_from_lb(pounds), 2)

    # Call the cm_from_in function to convert from inches to centimeters
    # and then round the result to one digit after the decimal.
    cm = round(cm_from_in(inches), 1)

    # Call the body_mass_index function and round
    # its result to one digit after the decimal.
    bmi = round(body_mass_index(kg, cm), 1)

    # Call the basal_metabolic_rate function and round
    # its result to an integer.
    bmr = round(basal_metabolic_rate(gender, kg, cm, years))

    # Print the results for the user to see.
    print("Age (years):", years)
    print("Weight (kg):", kg)
    print("Height (cm):", cm)
    print("Body mass index:", bmi)
    print("Basal metabolic rate (kcal/day):", bmr)


def compute_age(birth):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.datetime.strptime(birth, "%Y-%m-%d").date()
    today = datetime.datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

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
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()
