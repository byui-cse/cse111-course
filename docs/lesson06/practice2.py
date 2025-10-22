def count_cars_by_manufacturer(cars_data):
    """
    Return a list of all the manufacturers in cars_data
    and the number of cars made by each manufacturer.
    """

    # Create an empty dictionary that will hold the counters.
    manufacturers = {}

    # Unpack the data about each car.
    for vin, year, color, manufac, model in cars_data:

        if manufac not in manufacturers:
            # The manufacturer of the current car is NOT in
            # the dictionary, which means this is the first
            # car in the cars_data made by that manufacturer
            # so the count for that manufacturer should be 1.
            count = 1

        else:
            # The manufacturer of the current car is in the
            # dictionary so the new count is the previous
            # count plus one more.
            count = manufacturers[manufac] + 1

        # Store the new count in the dictionary.
        manufacturers[manufac] = count

    # Return a list of the manufacturers
    # and the number of cars made by each.
    return manufacturers.items()


def main():
    CARS = [
        # VIN, Manufacturer, Year Manufactured, Model, Color
        ["JT3HN86R6X0012345", "Toyota", 2019, "Tacoma", "Blue"],
        ["JTEBU5JR6K0123456", "Toyota", 2021, "4Runner", "Gray"],
        ["1HGCM82633A012345", "Honda", 2021, "Accord", "Blue"],
        ["1FTFW1EF2EFA12345", "Ford", 2018, "F-150", "White"],
        ["KNAGM4AD3F5012345", "Kia", 2020, "Optima", "Black"],
        ["JTMBFREV9HJ123456", "Toyota", 2020, "RAV4", "White"],
        ["5FNYF6H59KB123456", "Honda", 2021, "Pilot", "Green"]
    ]

    cars_by_manufac = count_cars_by_manufacturer(CARS)
    for manufac, count in cars_by_manufac:
        print(f"{manufac}: {count}")


if __name__ == "__main__":
    main()
