# Create variables of different data types.
a = False
b = "True"
c = 15
d = 7.6
e = c + d
f = "Her name is "
g = "Isabella"
h = f + g
i = input("Please enter a integer: ")
j = input("Please enter another integer: ")
k = i + j
m = float(input("Please enter a integer: "))
n = float(input("Please enter another integer: "))
p = m + n

# Print the variable names, data types, and values.
for key, value in {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g, "h":h,
        "i":i, "j":j, "k":k, "m":m, "n":n, "p":p}.items():
    print(key, type(value), value)

# Print a blank line.
print()

# Demonstrate some of the Python collection types.
x = "key"
y = "value"
print("''", type(''), len(''))
print('""', type(""), len(""))
print("()", type(()), len("()"))
print("[]", type([]), len("[]"))
print("{}", type({}), len("{}"))
print("(x)", type((x)), len(x))
print("(x,)", type((x,)), len((x,)))
print("[x]", type([x]), len([x]))
print("[x,]", type([x,]), len([x,]))
print("{x}", type({x}), len({x}))
print("{x,}", type({x,}), len({x,}))
print("{x:y}", type({x:y}), len({x:y}))
print("{x:y,}", type({x:y,}), len({x:y,}))

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

# Print a blank line.
print()

# Create five variables of different types. Create one each of
# string, range, point, list, and set.
message = "What a beautiful day!"
quant = range(10)
point = (-2, 1.4, 3)
names = ["Jason", "Britania", "Anders", "Takuya"]
colors = {"red", "green", "blue"}
students = {
    "67-412-8350":"Alan Benson",
    "76-420-1835":"Madison Silverlake",
    "06-412-7583":"Samyukta Daniels"
}

# Print the variable names, data types, and values.
for key, value in {"message":message, "quant":quant, "point":point,
        "names":names, "colors":colors, "students":students}.items():
    print(key, type(value), len(value), value)