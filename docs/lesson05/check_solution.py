import csv


def miles_per_gallon(start, end, gallons):
	"""Compute and return the average miles that
	a vehicle traveled per gallon of fuel."""
	mpg = abs(end - start) / gallons
	return mpg


def lp100k_from_mpg(mpg):
	"""Convert miles per gallon to liters per 100 kilometers."""
	lp100k = 235.215 / mpg
	return lp100k


def main():
	print("Date, Miles/Gallon, Liters/100 Km")
	with open("fuel_usage.csv", "rt") as fuel:
		reader = csv.reader(fuel)
		for row in reader:
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

				# Call a function to convert the miles per gallon
				# to liters per 100 kilometers.
				lp100k = lp100k_from_mpg(mpg)

				# Display the results for one row in the csv file.
				print(date, round(mpg, 1), round(lp100k, 2), sep=", ")


# Call the main function so that
# this program will start executing.
main()
