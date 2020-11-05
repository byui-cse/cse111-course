def write_text_file(filename, text):
    """Open a text file and write text to it."""
    with open(filename, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(text)


def read_text_file(filename):
    """Open a text file and read and return all the text from the file."""
    text = ""
    with open(filename, "rt", encoding="utf-8", newline="\n") as inf:
        text = inf.read()
    return text


def copy_text_file(source_filename, target_filename):
    """Copy the contents of one text file to another text file."""
    text = read_text_file(source_filename)
    write_text_file(target_filename, text)


def main():
    """Test the write_text_file and read_text_file functions to ensure
    they correctly write and read unicode characters besides English.
    """
    # Write text that contains Engligh, Greek,
    # and Deseret characters to a file.
    verse = \
"""For if ye forgive men their trespasses,
your heavenly Father will also forgive you.
ἐὰν γὰρ ἀφῆτε τοῖς ἀνθρώποις τὰ παραπτώματα αὐτῶν,
ἀφήσει καὶ ὑμῖν ὁ πατὴρ ὑμῶν ὁ οὐράνιος.
𐐙𐐫𐑉, 𐐮𐑁 𐐷 𐑁𐐲𐑉𐑀𐐮𐑂 𐑋𐐯𐑌 𐑄𐐯𐑉 𐐻𐑉𐐯𐑅𐐹𐐰𐑅𐐮𐑆,
𐐷𐐫𐑉 𐐸𐐯𐑂𐐲𐑌𐑊𐐨 𐐙𐐱𐑄𐐲𐑉 𐐶𐐮𐑊 𐐫𐑊𐑅𐐬 𐑁𐐲𐑉𐑀𐐮𐑂 𐐷𐐭.
"""
    write_text_file("forgive.txt", verse)

    # Read the text from the file that was just written
    # and print the text to verify that it is correct.
    text = read_text_file("forgive.txt")
    print(text)


# Call the main function so that
# this program will start executing.
main()
