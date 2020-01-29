# A list of people's height in meters.
heights = [1.72, 1.50, 1.96, 2.01, 1.75,
		2.11, 1.60, 1.65, 2.05, 1.50,
		1.80, 1.83, 2.05, 1.79, 1.84]

# Call the len, min, max, and sum functions and
# pass the list of heights to each function.
n = len(heights)
mn = min(heights)
mx = max(heights)
s = sum(heights)

# Round the result from the sum function.
s = round(s, 2)

# Display the results for the user to see.
print(f"len: {n}")
print(f"min: {mn}")
print(f"max: {mx}")
print(f"sum: {s}")
