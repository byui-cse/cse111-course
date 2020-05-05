# Create variables of different data types.
a = False
b = "True"
c = 15
d = 7.6
e = c + d
f = "Her name is "
g = "Isabella"
h = f + g
i = input("Please enter a number: ")
j = input("Please enter another number: ")
k = i + j
m = float(input("Please enter a number: "))
n = float(input("Please enter another number: "))
p = m + n

# Print the variable names, data types, and values.
for key, value in {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g, "h":h,
        "i":i, "j":j, "k":k, "m":m, "n":n, "p":p}.items():
    print(key, type(value), value)

# Print a blank line.
print()

# Create five variables of different types. Create
# one each of string, range, tuple, list, and set.
message = "What a beautiful day!"
quant = range(10)
point = (-2, 1.4, 3)
samples = [2.5, -3.2, 2.1, 0.6, 2.1, 0.7]
colors = {"red", "green", "blue"}
students = {
    "67-412-8350" : "Alan Benson",
    "76-240-1835" : "Madison Silverlake",
    "06-412-7583" : "Samyukta Daniels"
}

# Print the variable names, data types, and values.
for key, value in {"message":message, "quant":quant, "point":point,
        "samples":samples, "colors":colors, "students":students}.items():
    print(key, type(value), len(value), value)

# Print a blank line.
print()

# Demonstrate some of the Python collection types.
x = "key"
y = "value"
codes = [
    "''", '""',
    "()", "(x)", "(x,)",
    "[]", "[x]", "[x,]",
    "{}", "{x}", "{x,}",
    "{x:y}", "{x:y,}"
]
values = [
    '', "",
    (), (x), (x,),
    [], [x], [x,],
    {}, {x}, {x,},
    {x:y}, {x:y,}
]
for i, code in enumerate(codes):
    value = values[i]
    print(code, type(value), len(value), value)

# Print a blank line.
print()

# Demonstrate some of the conversion functions.
print("bool()", type(bool()))
print("int()", type(int()))
print("float()", type(float()))
print("str()", type(str()), len(str()))
print("tuple()", type(tuple()), len(tuple()))
print("list()", type(list()), len(list()))
print("set()", type(set()), len(set()))
print("dict()", type(dict()), len(dict()))
