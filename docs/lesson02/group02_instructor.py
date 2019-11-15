import json

iNumbers = [
	"75-176-2102",
	"05-205-8203",
	"32-302-1604",
	"25-104-1405",
	"00-115-2306",
]

names = [
	"James Smith",
	"Esther Einboden",
	"Cassidy Benavidez",
	"Joel Hatch",
	"Brianna Ririe",
]

nameFromINum = {
}

for i in range(0, len(iNumbers)):
	iNum = iNumbers[i]
	iNum = iNum.replace("-", "")
	iNumbers[i] = iNum
	nameFromINum[iNum] = names[i]

arrays = { "iNumbers":iNumbers, "names":names }

jsonArrays = json.dumps(arrays, indent=4, separators=(",", ":"))
jsonDict = json.dumps(nameFromINum, indent=4, separators=(",", ":"))

file = open("arrays.json", "wt")
file.write(jsonArrays)
file.write("\n")
file.close()

file = open("nameFromINum.json", "wt")
file.write(jsonDict)
file.write("\n")
file.close()

file = open("arrays.json", "rt")
arrays = json.loads(file.read())
file.close()
iNumbers = arrays["iNumbers"]
names = arrays["names"]
print(iNumbers)
print(names)
iNum = str(input("Please enter an I-Number (xx-xxx-xxxx): "))
index = -1
for i in range(0, len(iNumbers)):
	if (iNumbers[i] == iNum):
		index = i
		break
print(str(index) + " " + names[index])

file = open("dict.json", "rt")
nameFromINum = json.loads(file.read())
file.close()
print(nameFromINum)
iNum = str(input("Please enter an I-Number (xx-xxx-xxxx): "))
print(nameFromINum[iNum])