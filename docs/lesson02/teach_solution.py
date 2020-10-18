# Create a dictionary that holds product numbers and names.
products = {
    38500: "Backpacking Tent",
    27840: "Sit-Stand Desk",
    37992: "Mouse",
    24458: "Subwoofer",
    38323: "USB Cable",
    14392: "Monitor",
    11103: "Sleeping Bag",
    41023: "Cat-6 Network Cable",
    40246: "HDMI Cable",
    23047: "Keyboard",
    20319: "Keyboard",
    32061: "Mouse"
}

prod_num = ""
while not (len(prod_num) == 5 and prod_num.isdecimal()):
    # Get a product number from the user.
    prod_num = input("Please enter a product number: ")

    # Verify that the product number is valid.
    if not prod_num.isdigit():
        print("Invalid character in product number")
    elif len(prod_num) < 5:
        print("Invalid product number: too few digits")
    elif len(prod_num) > 5:
        print("Invalid product number: too many digits")

# The user input is a valid product number. Convert the product
# number from a string to an integer, so that this program can
# find the product number in the products dictionary.
prod_num = int(prod_num)

# Verify that the product number is in the products dictionary.
if prod_num in products:
    # Find the corresponding product name and print it.
    prod_name = products[prod_num]
    print(f"{prod_num}: {prod_name}")
else:
    print(f"No such product: {prod_num}")
