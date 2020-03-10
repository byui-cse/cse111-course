import re


def main():
    # Read the base words into a dictionary.
    base_words = read_base_words("base_words.txt")

    # A dictionary of base words and the number of times
    # each word appears in the text of the Book of Mormon.
    frequencies = {}

    with open("book_of_mormon.txt", "rt") as bom:
        for line in bom:
            if not is_heading(line):
                count_words_in_line(frequencies, line, base_words)

    # Create a list from the frequencies dictionary. Each
    # item in thelist is a tuple like this: (word, count).
    words = list(frequencies.items())

    # Sort the list of words by count (frequency).
    words.sort(reverse=True, key=lambda item: (item[1], item[0]))

    # Print tuples (word, count) for all words that
    # appear more than five times in the Book of Mormon.
    for item in words:
        if item[1] > 5:
            print(item)


def read_base_words(filename):
    """Read base words and their variants from a file and
    store them in a dictionary. Return the dictionary so
    that it can be passed into other functions.
    """
    base_words_dict = {}

    with open(filename, "rt") as infile:
        for line in infile:
            parts = line.strip().split(": ")
            base = parts[0]
            for word in parts[1].split(", "):
                base_words_dict[word] = base

    return base_words_dict


def get_base_word(base_words_dict, word):
    """Return the base of a word."""
    if word in base_words_dict:
        base = base_words_dict[word]
    else:
        base = word
    return base


# A pattern with global scope used to determine if
# a line of text is a chapter or verse heading.
heading_pattern = re.compile("^$|^([1-4] )?(Nephi|Jacob|Enos|Jarom|Omni|Words of Mormon|Mosiah|Alma|Helaman|Mormon|Ether|Moroni)( [1-9][0-9]?)?(:[1-9][0-9]?)?$")

def is_heading(text):
    """Return true if text is a scripture heading; otherwise return false."""
    return heading_pattern.match(text)


def count_words_in_line(frequencies, line, base_words):
    """For each word in line, increment the
    matching count in the frequencies dictionary.
    """
    line = remove_punct(line)
    for word in line.split():
        base = get_base_word(base_words, word)
        if base not in frequencies:
            frequencies[base] = 0
        frequencies[base] += 1


# Todo: instructions - ex: write a function to remove
# punctuation and test it on these ten strings.
def remove_punct(text):
    """Remove punctuation characters from text
    and return the text without the punctuation.
    """
    for ch in "(),;:.?!-":
        text = text.replace(ch, " ")
    text = text.replace("' ", " ").lower()
    text = text.replace("'s", " ")
    return text


# Todo: add a function to sort output by frequency or
# alphabetically, etc.


main()
