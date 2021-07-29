# Example 1

# Create variables of different data types and then
# print the variable names, data types, and values.

a = "Her name is "  # string
b = "Isabella"      # string
c = a + b           # string plus string makes string
print(f"a: {type(a)} {a}")
print(f"b: {type(b)} {b}")
print(f"c: {type(c)} {c}")
print()

d = False  # boolean
e = True   # boolean
print(f"d: {type(d)} {d}")
print(f"e: {type(e)} {e}")
print()

f = 15     # number
g = 7.62   # number
h = f + g  # number plus number makes number
print(f"f: {type(f)} {f}")
print(f"g: {type(g)} {g}")
print(f"h: {type(h)} {h}")
print()

i = "True"   # string because of the surrounding quotes
j = "2.718"  # string because of the surrounding quotes
print(f"i: {type(i)} {i}")
print(f"j: {type(j)} {j}")
print()

# The input function always returns a string.
k = input("Please enter a number: ")        # string
m = input("Please enter another number: ")  # string
n = k + m          # string plus string makes string
print(f"k: {type(k)} {k}")
print(f"m: {type(m)} {m}")
print(f"n: {type(n)} {n}")
print()

# The int and float functions convert a string to a number.
p = int(input("Please enter a number: "))          # number
q = float(input("Please enter another number: "))  # number
r = p + q                 # number plus number makes number
print(f"p: {type(p)} {p}")
print(f"q: {type(q)} {q}")
print(f"r: {type(r)} {r}")

# Print a blank line.
print()

# Demonstrate some of the conversion functions.
b = bool()
i = int()
f = float()
s = str()

# Print the variable names, data types, length, and values.
print(f"bool():  {type(b)}  {b}")
print(f"int():   {type(i)}   {i}")
print(f"float(): {type(f)} {f}")
print(f"str():   {type(s)} {len(s)} {s}")

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
