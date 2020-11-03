import math


# Make a boolean variable that will change to
# True after the user enters a valid integer.
valid = False

# The minimum and maximum integers that the user may enter.
minimum = 1

# Repeatedly ask the user to enter an integer until the
# user enters one between minimum and maximum, inclusive.
while not valid:
    text = input(f"Enter the number of items: ")

    # Determine if all the characters that
    # the user entered are decimal digits.
    if text.isdecimal():

        # Convert the text that the user
        # entered from a string to an integer.
        num_items = int(text)

        # Determine if the integer entered by the
        # user is between minimum and maximum, inclusive.
        if num_items < minimum:
            print(f"{num_items} is too small. Please"
                    " enter another positive integer.")
        else:
            # If the computer gets to this line of code, the user entered
            # an integer between minimum and maximum, so change the boolean
            # variable to True so that the loop will stop repeating.
            valid = True

    else:
        # The user entered at least one character that is not a decimal
        # digit, so print a message asking the user to enter an integer.
        print(f"'{text}' is not a positive integer."
            " Please enter a positive integer.")

# Print a blank line.
print()


# Make a boolean variable that will change to
# True after the user enters a valid integer.
valid = False

# The minimum and maximum integers that the user may enter.
minimum = 1

# Repeatedly ask the user to enter an integer until the
# user enters one between minimum and maximum, inclusive.
while not valid:
    text = input(f"Enter the number of items per box: ")

    # Determine if all the characters that
    # the user entered are decimal digits.
    if text.isdecimal():

        # Convert the text that the user
        # entered from a string to an integer.
        items_per_box = int(text)

        # Determine if the integer entered by the
        # user is between minimum and maximum, inclusive.
        if items_per_box < minimum:
            print(f"{items_per_box} is to small. Please"
                    " enter another positive integer.")
        else:
            # If the computer gets to this line of code, the user entered
            # an integer between minimum and maximum, so change the boolean
            # variable to True so that the loop will stop repeating.
            valid = True

    else:
        # The user entered at least one character that is not a decimal
        # digit, so print a message asking the user to enter an integer.
        print(f"'{text}' is not a positive integer."
            " Please enter a positive integer.")

# Print a blank line.
print()


# Compute the number of boxes.
num_boxes = math.ceil(num_items / items_per_box)

# Display the results for the user to see.
print(f"For {num_items} items, packing {items_per_box}"
f" items in each box, you will need {num_boxes} boxes.")

# Print a blank line.
print()
