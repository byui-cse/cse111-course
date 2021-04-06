def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name".
    For example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".
    """
    return f"{family_name};{given_name}"


def extract_family_name(full_name):
    """Extract and return the family name from a
    string in this form "family_name; given_name".
    For example, if this function were called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    return full_name[0 : semicolon_index]


def extract_given_name(full_name):
    """Extract and return the given name from a
    string in this form "family_name; given_name".
    For example, if this function were called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("/ ")

    # Extract a substring from the full name and return it.
    return full_name[semicolon_index + 2 : ]
