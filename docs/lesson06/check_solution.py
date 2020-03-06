import random

def main():
	randnums = [16.2, 75.1, 52.3]
	print(f"randnums {randnums}")

	# Add one random number to the list randnums.
	append_random_numbers(randnums)
	print(f"randnums {randnums}")

	# Add three random numbers to the list randnums.
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


main()
