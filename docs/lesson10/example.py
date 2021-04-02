# Import the math module so we can use math.pi and math.sqrt.
import math

# Print a description of this program.
print("This program computes and outputs the")
print("surface area of a right circular cone.")
print()

# The minimum and maximum integers that the
# user may enter for the radius of a cone.
minimum = 2
maximum = 500

# Make a boolean variable that will change to
# True after the user enters a valid integer.
valid = False

# Repeatedly ask the user to enter an integer until the
# user enters one between minimum and maximum, inclusive.
while not valid:
    text = input("Enter the integer radius of a cone: ")

    # Determine if all the characters that
    # the user entered are decimal digits.
    if text.isdecimal():

        # Convert the text that the user
        # entered from a string to an integer.
        radius = int(text)

        # Determine if the integer entered by the
        # user is between minimum and maximum, inclusive.
        if radius < minimum:
            print(f"{radius} is too small. Please enter a positive"
                    f" integer between {minimum} and {maximum}.")
        elif radius > maximum:
            print(f"{radius} is too large. Please enter a positive"
                    f" integer between {minimum} and {maximum}.")
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

# The minimum and maximum integers that the
# user may enter for the height of a cone.
minimum = 3
maximum = 1000

# Make a boolean variable that will change to
# True after the user enters a valid integer.
valid = False

# Repeatedly ask the user to enter an integer until the
# user enters one between minimum and maximum, inclusive.
while not valid:
    text = input("Enter the integer height of a cone: ")

    # Determine if all the characters that
    # the user entered are decimal digits.
    if text.isdecimal():

        # Convert the text that the user
        # entered from a string to an integer.
        height = int(text)

        # Determine if the integer entered by the
        # user is between minimum and maximum, inclusive.
        if height < minimum:
            print(f"{height} is too small. Please enter a positive"
                    f" integer between {minimum} and {maximum}.")
        elif height > maximum:
            print(f"{height} is too large. Please enter a positive"
                    f" integer between {minimum} and {maximum}.")
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


# Compute the surface area of the cone.
radical = math.sqrt(radius**2 + height**2)
surf_area = math.pi * radius * (radius + radical)

# Print the surface area rounded to one digit
# after the decimal point for the user to see.
print(f"The surface area is {surf_area:.1f}")
