import datetime

# Get the subtotal from the user.
text = input("Please enter the subtotal: ")
subtotal = float(text)

# Get the day of the week from the computer's clock.
dayOfWeek = datetime.datetime.now().weekday()

discRate = 0.10
salesTaxRate = 0.06

if subtotal > 50 and (dayOfWeek == 2 or dayOfWeek == 3):
	discount = round(subtotal * discRate, 2)
	subtotal -= discount
salesTax = round(subtotal * salesTaxRate, 2)
total = subtotal + salesTax

# Display the total for the user to see.
print(total)
