"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

# Get the user's age as a string.
text = input("Please enter your age: ")

# Convert the string that the user entered into an integer.
age = int(text)

# Compute the slowest and fastest beneficial
# heart rates from the user's age.
maxRate = 220 - age
slowest = round(maxRate * 0.65)
fastest = round(maxRate * 0.85)

# Use f-strings to create a message for the user to see.
message = \
    f"When you exercise to strengthen your heart, you should keep\n" \
    f"your heart rate between {slowest} and {fastest} beats per minute."

# Print the message.
print(message)
