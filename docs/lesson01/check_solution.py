# Get the user's age as a string.
text = input("Please enter your age: ")

# Convert the string that the user entered into a positive integer.
age = abs(round(float(text)))

# Compute the slowest and fastest beneficial heart rates for the user.
maxRate = 220 - age
slowest = round(maxRate * 0.65)
fastest = round(maxRate * 0.85)

# Use f-strings to create a message for the user to see.
print(
	f"When you exercise to strengthen your heart, you should keep\n"
	f"your heart rate between {slowest} and {fastest} beats per minute."
)
