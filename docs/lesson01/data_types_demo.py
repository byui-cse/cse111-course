# Create variables of different data types.
a = False   # boolean
b = "True"  # string
c = 15          # number
d = 7.6         # number
e = c + d       # number
f = "Her name is "  # string
g = "Isabella"      # string
h = f + g           # string
i = input("Please enter a number: ")        # string
j = input("Please enter another number: ")  # string
k = i + j                                   # string
m = float(input("Please enter a number: "))         # number
n = float(input("Please enter another number: "))   # number
p = m + n                                           # number

# Print the variable names, data types, and values.
print(a, type(a), a)
print(b, type(b), b)
print(c, type(c), c)
print(d, type(d), d)
print(e, type(e), e)
print(f, type(f), f)
print(g, type(g), g)
print(h, type(h), h)
print(i, type(i), i)
print(j, type(j), j)
print(k, type(k), k)
print(m, type(m), m)
print(n, type(n), n)
print(p, type(p), p)

# Print a blank line.
print()

# Demonstrate some of the conversion functions.
b = bool()
i = int()
f = float()
s = str()

# Print the variable names, data types, length, and values.
print("bool()", type(b), b)
print("int()", type(i), i)
print("float()", type(f), f)
print("str()", type(s), len(s), s)

# Print a blank line.
print()

# Demonstrate some of the Python collection types.
# Create one each of list, and dictionary.
samples = [2.5, -3.2, 2.1, 0.6, 2.1, 0.7]
students = {
    "67-412-8350" : "Alan Benson",
    "76-240-1835" : "Madison Silverlake",
    "06-412-7583" : "Samyukta Daniels"
}

# Print the variable names, data types, length, and values.
print("samples", type(samples), len(samples), samples)
print("students", type(students), len(students), students)

# Print a blank line.
print()

# Demonstrate the empty string, empty list, and empty dictionary.
empty_string1 = ''
empty_string2 = ""
empty_string3 = str()
empty_list1 = []
empty_list2 = list()
empty_dict1 = {}
empty_dict2 = dict()

# Print the variable names, data types, length, and values.
print("empty_string1", type(empty_string1), len(empty_string1), empty_string1)
print("empty_string2", type(empty_string2), len(empty_string2), empty_string2)
print("empty_string3", type(empty_string3), len(empty_string3), empty_string3)
print("empty_list1", type(empty_list1), len(empty_list1), empty_list1)
print("empty_list2", type(empty_list2), len(empty_list2), empty_list2)
print("empty_dict1", type(empty_dict1), len(empty_dict1), empty_dict1)
print("empty_dict2", type(empty_dict2), len(empty_dict2), empty_dict2)
