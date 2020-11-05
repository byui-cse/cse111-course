import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(f"randnums {randnums}")

    # Call the append_random_numbers function to
    # add one random number to the randnums list.
    append_random_numbers(randnums)
    print(f"randnums {randnums}")

    # Call the append_random_numbers function to add
    # three random numbers to the randnums list.
    append_random_numbers(randnums, 3)
    print(f"randnums {randnums}")


def append_random_numbers(numbers_list, quantity=1):
    """ Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


# Call the main function so that
# this program will start executing.
main()
