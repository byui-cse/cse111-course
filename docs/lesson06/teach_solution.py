import re

# A dictionary with global scope that holds words and their bases.
base_from_word = {}

# A pattern with global scope used to determine if
# a line of text is a chapter or verse heading.
pattern = re.compile("^$|^([1-4] )?(Nephi|Jacob|Enos|Jarom|Omni|Words of Mormon|Mosiah|Alma|Helaman|Mormon|Ether|Moroni)( [1-9][0-9]?)?(:[1-9][0-9]?)?$")


def read_base_words(filename):
	"""Read words and their bases from
	a file and store them in a dictionary.
	"""
	with open(filename, "rt") as infile:
		for line in infile:
			parts = line.strip().split(": ")
			base = parts[0]
			for word in parts[1].split(", "):
				base_from_word[word] = base


def get_base_word(word):
	"""Return the base of a word."""
	if word in base_from_word:
		base = base_from_word[word]
	else:
		base = word
	return base


def is_heading(text):
	"""Return true if text is a scripture heading; otherwise return false."""
	return pattern.match(text)


def remove_punct(text):
	"""Remove punctuation characters from text"""
	for ch in "(),;:.?!-":
		text = text.replace(ch, " ").lower()
	text = text.replace("' ", " ")
	text = text.replace("'s", " ")
	return text


def main():
	read_base_words("base_words.txt")

	# A dictionary of base words and the number of times
	# those words appear in the text of the Book of Mormon.
	frequencies = {}

	with open("book_of_mormon.txt", "rt") as bom:
		for line in bom:
			line = line.strip()
			if not is_heading(line):
				line = remove_punct(line)
				for word in line.split():
					base = get_base_word(word)
					if base not in frequencies:
						frequencies[base] = 0
					frequencies[base] += 1

	# Create a list from the frequencies dictionary.
	words = list(frequencies.items())

	# Sort the list of words by count.
	words.sort(reverse=True, key=lambda item: (item[1], item[0]))

	# Print (word, count) tuples for all words that
	# appear more than five times in the Book of Mormon.
	for item in words:
		if item[1] > 5:
			print(item)


main()
