# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def prefix(string1, string2):
    """Return the prefix, if any, that appears in both string1 and
    string2. In other words, return a string of the characters
    that appear at the beginning of both string1 and string2. For
    example, if string1 is "inconceivable" and string2 is
    "inconvenient", this function will return "incon".

    Parameters
        string1: a string of text
        string2: another string of text
    Return: a string
    """
    # Convert both strings to lower case.
    string1 = string1.lower()
    string2 = string2.lower()

    # Start at the beginning of both strings.
    i = 0

    # Repeat until the computer finds two
    # characters that are not the same.
    limit = min(len(string1), len(string2))
    while i < limit:
        if string1[i] != string2[i]:
           break
        i += 1

    # Extract a substring from string1 and return it.
    pre = string1[0 : i]
    return pre


def suffix(string1, string2):
    """Return the suffix, if any, that appears in both string1 and
    string2. In other words, return a string of the characters
    that appear at the end of both string1 and string2. For
    example, if string1 is "hilarious" and string2 is "nefarious",
    this function will return "arious".

    Parameters
        string1: a string of text
        string2: another string of text
    Return: a string
    """
    # Convert both strings to lower case.
    string1 = string1.lower()
    string2 = string2.lower()

    # Start at the end of both strings.
    i1 = len(string1) - 1
    i2 = len(string2) - 1

    # Repeat until the computer finds two
    # characters that are not the same.
    limit = min(len(string1), len(string2))
    for _ in range(limit):
        if string1[i1] != string2[i2]:
            break
        i1 -= 1
        i2 -= 1

    # Extract a substring from string1 and return it.
    suf = string1[i1+1 : ]
    return suf
