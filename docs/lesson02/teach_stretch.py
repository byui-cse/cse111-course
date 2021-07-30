"""
You work for a retail store that wants to increase sales on Tuesday and
Wednesday, which are the store's slowest sales days. On Tuesday and
Wednesday, if a customer's subtotal is greater than $50, the store will
discount the customer's purchase by 10%.
"""

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# The discount rate is 10% and the sales tax rate is 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = 0

text = ""
while text.lower() != "done":
    # Get the price from the user.
    text = input("Please enter the price: ")
    if text.lower() != "done":
        price = float(text)

        # Get the quantity from the user.
        quantity = int(input("Please enter the quantity: "))

        subtotal += price * quantity

        # Print a blank line.
        print()

# Round the subtotal to two digits after
# the decimal and print the subtotal.
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal}")
print()

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date_and_time = datetime.now()

# Call the isoweekday() method to get the day of
# the week from the current_date_and_time object.
weekday = current_date_and_time.isoweekday()

# if the subtotal is greater than 50 and
# today is Tuesday or Wednesday, compute the discount.
if weekday == 2 or weekday == 3:
    if subtotal < 50:
        insufficient = 50 - subtotal
        print(f"To receive the discount, add {insufficient} to your order.")
    else:
        discount = round(subtotal * DISC_RATE, 2)
        print(f"Discount amount: {discount}")
        subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax}")

# Compute the total by adding the subtotal and the sales tax.
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")
