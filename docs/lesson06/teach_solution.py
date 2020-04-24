import requests


def read_text_file(pathname):
    """Open, read, and return all the text from a text file."""
    text = ""
    with open(pathname, mode="rt", encoding="utf-8", newline="\n") as inf:
        text = inf.read()
    return text


def write_text_file(pathname, text):
    """Open a text file and write text to it."""
    with open(pathname, mode="wt", encoding="utf-8", newline="\n") as outf:
        outf.write(text)


def test_io():
    """Test the write_text_file and read_text_file functions to ensure
    they correctly write and read unicode characters besides English.
    """
    # Write text that contains Engligh, Greek,
    # and Deseret characters to a file.
    matt_6_14 = \
"""For if ye forgive men their trespasses,
your heavenly Father will also forgive you.
ἐὰν γὰρ ἀφῆτε τοῖς ἀνθρώποις τὰ παραπτώματα αὐτῶν,
ἀφήσει καὶ ὑμῖν ὁ πατὴρ ὑμῶν ὁ οὐράνιος.
𐐙𐐫𐑉, 𐐮𐑁 𐐷 𐑁𐐲𐑉𐑀𐐮𐑂 𐑋𐐯𐑌 𐑄𐐯𐑉 𐐻𐑉𐐯𐑅𐐹𐐰𐑅𐐮𐑆,
𐐷𐐫𐑉 𐐸𐐯𐑂𐐲𐑌𐑊𐐨 𐐙𐐱𐑄𐐲𐑉 𐐶𐐮𐑊 𐐫𐑊𐑅𐐬 𐑁𐐲𐑉𐑀𐐮𐑂 𐐷𐐭.
"""
    write_text_file("forgive.txt", matt_6_14)

    # Read the text from the file that was just written
    # and print the text to verify that it is correct.
    text = read_text_file("forgive.txt")
    print(text)


def make_text_filename(basename, lang):
    """Build and return a filename for a text file from a basename
    and a language abbreviation. For example, if basename is "sermon"
    and lang is "es", this function will return "sermon_es.txt".
    """
    return f"{basename}_{lang}.txt"


def translate(text, src_lang, targ_lang):
    """Send text to an online machine translation
    service and return the translated text.
    """
    endpoint = "https://translate.yandex.net/api/v1.5/tr.json/translate"

    args = {
        # The API key should remain private. Do not save
        # it to a public repository or public web site.
        "key" : "The API key is in your I-Learn course.",

        "lang" : f"{src_lang}-{targ_lang}"
    }

    transl = ""
    response = requests.post(endpoint, params=args, data={"text":text})
    if response.status_code == 200:
        # If the request was successful, retrieve
        # the translated text from the response.
        data = response.json()
        transl = data["text"][0]
    else:
        # If the request was not successful, print the status code.
        print(response.status_code)

    return transl


def main():
    src_lang = "en"
    targ_lang = "pt"
    basenames = ["sermon", "upward", "numsys"]
    for name in basenames:
        inname = make_text_filename(name, src_lang)
        orig_text = read_text_file(inname)

        transl_text = translate(orig_text, src_lang, targ_lang)

        outname = make_text_filename(name, targ_lang)
        write_text_file(outname, transl_text)


main()
