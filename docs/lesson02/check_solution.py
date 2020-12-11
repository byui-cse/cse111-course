"""
You work for a retail store that wants to increase sales on Tuesday and
Wednesday, which are the store's slowest sales days. On Tuesday and
Wednesday, if a customer's subtotal is greater than $50, the store will
discount the customer's purchase by 10%.
"""

# Import the datatime module so that it can be used in this program.
import datetime

# Get the subtotal from the user.
text = input("Please enter the subtotal: ")
subtotal = float(text)

# Get the day of the week from the computer's clock.
weekday = datetime.datetime.now().isoweekday()

# The discount rate is 10% and the sales tax rate is 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

# if the subtotal is greater than 50 and
# today is Tuesday or Wednesday, compute the discount.
if subtotal > 50 and (weekday == 2 or weekday == 3):
    discount = round(subtotal * DISC_RATE, 2)
    subtotal -= discount

# Compute the sales tax and total. Notice that we compute the sales
# tax after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")
