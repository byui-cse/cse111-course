import csv

# Read the I-Numbers and names from the
# CSV file and add them to a dictionary.
students = {}
with open("students.csv", "rt") as infile:
    reader = csv.reader(infile, delimiter=",")
    for row in reader:
        if reader.line_num > 1:
            students[row[0]] = row[1]

# Get an I-Number from the user.
text = str(input("Please enter an I-Number (xx-xxx-xxxx): "))

# The I-Numbers are stored in the CSV file as digits only (without any
# dashes), so we remove all non-digit characters from the user's input.
# Also, count the number of invalid characters.
ninvalid = 0
inum = ""
for c in text:
    if c.isdigit():
        inum += c
    elif c != "-":
        ninvalid += 1

# Determine if the user input is formatted correctly.
if len(inum) == 9 and ninvalid == 0:
    # The user input is a valid I-Number. Find
    # the I-Number in the list of I-Numbers.
    if inum in students:
        # Print the student name that corresponds
        # to the I-Number that the user input.
        name = students[inum]
        print(name)
    else:
        print("No such student")
else:
    # The user input is invalid.
    if ninvalid > 0:
        errmsg = "Invalid character in I-Number"
    elif len(inum) < 9:
        errmsg = "Invalid I-Number: too few digits"
    elif len(inum) > 9:
        errmsg = "Invalid I-Number: too many digits"
    print(errmsg)
