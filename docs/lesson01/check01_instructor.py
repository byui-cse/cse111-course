# Get the user's age as a string.
text = input("Please enter your age: ")

# Convert the string that the user entered into an integer.
age = int(text)

# Compute the slowest and fastest beneficial heart rates for the user.
maxRate = 220 - age
slowest = round(maxRate * 0.65)
fastest = round(maxRate * 0.85)

# Use string concatenation to create a message for the user to see.
output = "When you exercise, you should keep your heart rate between " \
		+ str(slowest) + " and " + str(fastest) + " beats per minute."
print(output)
