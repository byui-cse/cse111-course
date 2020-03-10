def prefix(s1, s2):
    """Return the prefix, if any, that appears in both s1 and s2. In
    other words, return a string of the characters that appear at the
    beginning of both s1 and s2. For example, if s1 is "inconceivable"
    and s2 is "inconvenient", this function will return "incon".
    """
    s1 = s1.lower()
    s2 = s2.lower()
    i = 0
    limit = min(len(s1), len(s2))
    while i < limit:
        if s1[i] != s2[i]:
            break
        i += 1
    return s1[0:i]


def suffix(s1, s2):
    """Return the suffix, if any, that appears in both s1 and s2. In
    other words, return a string of the characters that appear at the
    end of both s1 and s2. For example, if s1 is "hilarious" and s2 is
    "nefarious", this function will return "arious".
    """
    s1 = s1.lower()
    s2 = s2.lower()
    i1 = len(s1) - 1
    i2 = len(s2) - 1
    limit = min(len(s1), len(s2))
    for _ in range(limit):
        if s1[i1] != s2[i2]:
            break
        i1 -= 1
        i2 -= 1
    return s1[i1 + 1:]
