"""
Given a list of cars, count and print the number of cars
that were built by each different manufacturer.
"""

def main():
    cars_list = [
        # VIN, Manufacturer, Year Manufactured, Model, Color
        ["JT3HN86R6X0012345", "Toyota", 2019, "Tacoma", "Blue"],
        ["JTEBU5JR6K0123456", "Toyota", 2021, "4Runner", "Gray"],
        ["1HGCM82633A012345", "Honda", 2021, "Accord", "Blue"],
        ["1FTFW1EF2EFA12345", "Ford", 2018, "F-150", "White"],
        ["KNAGM4AD3F5012345", "Kia", 2020, "Optima", "Black"],
        ["JTMBFREV9HJ123456", "Toyota", 2020, "RAV4", "White"],
        ["5FNYF6H59KB123456", "Honda", 2021, "Pilot", "Green"]
    ]

    cars_by_manufac_list = count_cars_by_manufacturer(cars_list)
    for manufac, count in cars_by_manufac_list:
        print(f"{manufac}: {count}")


def count_cars_by_manufacturer(cars_list):
    """
    Return a list of all the manufacturers in cars_list
    and the number of cars made by each manufacturer.
    """
    # Create an empty dictionary that will hold the counters.
    manufacturers_dict = {}

    # Unpack the data about each car.
    for vin, year, color, manufac, model in cars_list:

        if manufac not in manufacturers_dict:
            # The manufacturer of the current car is NOT in
            # the dictionary, which means this is the first
            # car in the cars_list made by that manufacturer
            # so the count for that manufacturer should be 1.
            count = 1

        else:
            # The manufacturer of the current car is in the
            # dictionary so the new count is the previous
            # count plus one more.
            count = manufacturers_dict[manufac] + 1

        # Store the new count in the dictionary.
        manufacturers_dict[manufac] = count

    # Return a list of the manufacturers
    # and the number of cars made by each.
    return manufacturers_dict.items()


if __name__ == "__main__":
    main()
