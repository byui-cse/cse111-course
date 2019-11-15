import json

iNumbers = [
	"75-176-6201",
	"75-176-2102",
	"05-205-8203",
	"32-302-1604",
	"25-104-1405",
	"00-115-2306",
	"18-270-6207",
	"12-471-2708",
	"21-250-5409",
]

names = [
	"James Smith",
	"Esther Einboden",
	"Cassidy Benavidez",
	"Joel Hatch",
	"Brianna Ririe",
	"Stefano Hisler",
	"Hyeonbeom Park",
	"Maren Thomas",
	"Tyler Clark",
]

nameFromINum = {
}

# Populate the dictionary.
for i in range(0, len(iNumbers)):
	iNum = iNumbers[i]
	nameFromINum[iNum] = names[i]

# Convert both lists and the dictionary to JSON.
jsonINums = json.dumps(iNumbers, indent=4, separators=(",", ":"))
jsonNames = json.dumps(names, indent=4, separators=(",", ":"))
jsonDict = json.dumps(nameFromINum, indent=4, separators=(",", ":"))

# Write both lists and the dictionary to text files.
file = open("inumbers.json", "wt")
file.write(jsonINums)
file.write("\n")
file.close()

file = open("names.json", "wt")
file.write(jsonNames)
file.write("\n")
file.close()

file = open("dict.json", "wt")
file.write(jsonDict)
file.write("\n")
file.close()
