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


def append_random_numbers(ls, n=1):
    """ Append n random numbers onto the list ls. The
    random numbers are between 0 and 100, inclusive.
    """
    for _ in range(n):
        num = random.uniform(0, 100)
        rounded = round(num, 1)
        ls.append(rounded)


# Call the main function so that
# this program will start executing.
main()
