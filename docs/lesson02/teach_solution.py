filename = "responses.txt"
print(filename)

# Create an empty list that will hold the
# responses that are read from the file.
responses = []

# Open the responses.txt file.
with open(filename, "rt") as textfile:

    # Each line in the file contains one response which is a number.
    for line in textfile:
        # For each line in the file, convert
        # the text from a string to a number.
        response = float(line)

        # Skip all responses that are less than zero.
        if response >= 0:
            # Store the number in the responses list.
            responses.append(response)

# Compute the quantity, sum, and average of the responses.
quantity = len(responses)
total = sum(responses)
average = total / quantity

# Display the average for the user to see.
print(f"There are {quantity} responses with an average value of {round(average, 2)}")

# Count how many responses are greater than the average.
count = 0
for response in responses:
    if response > average:
        count += 1

# Display the number of responses that are greater than the average.
print(f"{count} of the responses are greater than the average.")
