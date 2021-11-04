# Import the sleep function from the time module, so
# that the sleep function can be used in this program.
from time import sleep

# Prompt the user to enter her name.
name = input("Hello! What is your name? ")

# Print the numbers 3, 2, 1.
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)  # Pause for 1/2 second

# Use a Python f-string to format a greeting
# for the user and then print the greeting.
print(f"Welcome to CSE 111, {name}!")
