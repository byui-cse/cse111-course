import csv
import math
from datetime import date, datetime


def compute_age(birthdate):
	"""Compute and return a person's age in years."""
	now = date.today()
	diff = now - birthdate
	years = math.floor(diff.days / 365.25)
	return years


def body_mass_index(weight, height):
	"""Calculate and return a person's body mass index (bmi). weight
	and height must be in kilograms and centimeters, respectively."""
	bmi = weight / (height ** 2) * 10000
	return bmi


def basal_metabolic_rate(gender, weight, height, age):
	"""Calculate and return a person's basal metabolic rate (bmr). age
	must be in years, weight must be in kilograms, and height must be in
	centimeters."""
	if gender.upper() == "F":
		bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
	else:
		bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
	return bmr


def kg_from_lb(lb):
	"""Convert a mass in pounds to kilograms."""
	kg = lb * 0.453592
	return kg

def cm_from_in(inch):
	"""Convert a length in inches to centimeters."""
	cm = inch * 2.54
	return cm


def main():
	with open("fitness.csv", "rt") as fitness:
		reader = csv.reader(fitness)
		for row in reader:
			if reader.line_num > 1:
				gender = row[0]

				birth = datetime.strptime(row[1], "%Y-%m-%d").date()
				years = compute_age(birth)

				pounds = float(row[2])
				inches = float(row[3])
				kg = round(kg_from_lb(pounds), 2)
				cm = round(cm_from_in(inches), 1)

				bmi = round(body_mass_index(kg, cm), 1)
				bmr = round(basal_metabolic_rate(gender, kg, cm, years), 1)
				print(gender, years, kg, cm, bmi, bmr, sep=", ")


main()
