import datetime

# Get the subtotal from the user.
text = input("Please enter the subtotal: ")
subtotal = float(text)

# Get the day of the week from the computer's clock.
weekday = datetime.datetime.now().isoweekday()

# The discount rate is 10% and the sales tax rate is 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

# Compute the discount if applicable.
if subtotal > 50 and (weekday == 2 or weekday == 3):
	discount = round(subtotal * DISC_RATE, 2)
	subtotal -= discount

# Compute the sales tax and total. Notice that we compute the sales tax
# after computing the discount because the customer does not pay sales
# tax on the full price but on the discounted price.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
total = round(subtotal + sales_tax, 2)

# Display the total for the user to see.
print(f"Total: {total}")
