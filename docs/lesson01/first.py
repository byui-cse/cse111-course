def makeMultiplier(n):
	return lambda a : a * n

doubler = makeMultiplier(2)
tripler = makeMultiplier(3)
print(doubler(11))
print(tripler(11))


def insertSort(list, compare):
	first = 0
	last = len(list) - 1
	i = last - 1
	while i >= first:
		swap = list[i]
		j = i + 1
		while j <= last:
			cmp = compare(swap, list[j])
			if cmp <= 0:
				break
			list[j - 1] = list[j]
			j += 1
		list[j - 1] = swap
		i -= 1

# In python, lambdas are not allowed to use
# statements. They can use expressions only.
compareNumbers = lambda x, y : y - x
compareStrings = lambda s, t : -1 if s < t else (1 if s > t else 0)
#compareIgnoreCase = lambda s, t : -1 if s.lower() < t.lower() else (1 if s.lower() > t.lower() else 0)

def compareIgnoreCase(s, t):
	s = s.upper()
	t = t.upper()
	return -1 if s < t else (1 if s > t else 0)

def main():
	numbers = [ 7, 10, 8, 16, 3, 35 ]
	vegetables = [ "Radish", "Carrot", "Tomato", "Pea" ]
	names = [ "Samuel", "NiCole", "Mitchell", "Nick" ]

	insertSort(numbers, compareNumbers)
	print(numbers)

	insertSort(vegetables, compareStrings)
	print(vegetables)

	insertSort(names, compareStrings)
	print(names)
	insertSort(names, compareIgnoreCase)
	print(names)

if __name__ == "__main__":
	main()
