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
inum = str(input("Please enter an I-Number (xx-xxx-xxxx): "))

# The I-Numbers are stored in the CSV file as digits only (without
# any dashes), so we remove all dashes from the user's input.
inum = inum.replace("-", "")

# Determine if the user input is formatted correctly.
if inum.isdigit():
    if len(inum) < 9:
        print("Invalid I-Number: too few digits")
    elif len(inum) > 9:
        print("Invalid I-Number: too many digits")
    else:
        # The user input is a valid I-Number. Find
        # the I-Number in the list of I-Numbers.
        if inum in students:
            # Print the student name that corresponds
            # to the I-Number that the user entered.
            name = students[inum]
            print(name)
        else:
            print("No such student")
else:
    print("Invalid character in I-Number")
