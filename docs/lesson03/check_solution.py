"""
Write a Python program named provinces.py that reads the contents
of provinces.txt into a list and that modifies the list.
"""

# Open the provinces.txt text file for reading.
with open("provinces.txt", "rt") as infile:

    # Read all the lines of the file into a list
    # named provinces. Each line of the file will
    # be stored in its own element in the list.
    string = infile.read()
    provinces = string.splitlines()

# As a debugging aid, print the entire list.
print(provinces)
print()

# Remove the first element from the list.
provinces.pop(0)
#print(provinces)

# Remove the last element from the list.
provinces.pop()
#print(provinces)

# Replace all occurrrences of "AB" with "Alberta".
for i in range(len(provinces)):
    if provinces[i] == "AB":
        provinces[i] = "Alberta"
#print(provinces)

# Count the number of elements that are "Alberta"
count = 0
for province in provinces:
    if province == "Alberta":
        count += 1

print(f"Alberta occurs {count} times in the modified list.")
