import datetime

# Get the subtotal from the user.
text = input("Please enter the subtotal: ")
subtotal = float(text)

# Get the day of the week from the computer's clock.
dayOfWeek = datetime.datetime.now().weekday()

# The discount rate is 10% and the sales tax rate is 6%.
discRate = 0.10
salesTaxRate = 0.06

# Compute the discount if applicable.
if subtotal > 50 and (dayOfWeek == 2 or dayOfWeek == 3):
	discount = round(subtotal * discRate, 2)
	subtotal -= discount

# Compute the sales tax and total.
salesTax = round(subtotal * salesTaxRate, 2)
total = subtotal + salesTax

# Display the total for the user to see.
print(total)
