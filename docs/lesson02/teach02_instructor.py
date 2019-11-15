import json

# Read the I-Numbers list from the JSON
# file and convert it from JSON to a list.
file = open("inumbers.json", "rt")
iNumbers = json.loads(file.read())
file.close()

# Read the names list from the JSON file
# and convert it from JSON to a list.
file = open("names.json", "rt")
names = json.loads(file.read())
file.close()

# Get an I-Number from the user.
iNum = str(input("Please enter an I-Number (xx-xxx-xxxx): "))

# Count the number of digits in the user input.
ndigits = 0
for c in iNum:
	if c.isdigit():
		ndigits += 1

# Determine if the user input is formatted correctly.
if len(iNum) == 11 and ndigits == 9 and iNum[2] == '-' and iNum[6] == '-':
	# The user input is formatted correctly.
	pass
else:
	# The user input is formatted incorrectly.
	if ndigits < 9:
		print("Invalid I-Number: too few digits")
	elif ndigits > 9:
		print("Invalid I-Number: too many digits")
	else:
		# The given I-Number contains the correct number of digits, but
		# is formatted incorrectly, so reformat it.

		# First copy only the digits from the given I-Number.
		digits = ""
		for c in iNum:
			if c.isdigit():
				digits += c

		# Second use the original digits to create
		# a new I-Number that is formatted correctly.
		iNum = digits[0] + digits[1] + "-" + \
				digits[2] + digits[3] + digits[4] + "-" + \
				digits[5] + digits[6] + digits[7] + digits[8]

if ndigits == 9:
	# Find the I-Number in the list of I-Numbers.
	if iNum in iNumbers:
		# Print the student name that corresponds
		# to the I-Number that the user input.
		index = iNumbers.index(iNum)
		print(names[index])
	else:
		print("No such student")
