import os.path
import re
import sys


def main(argv):
    srcparts = splitpath(argv[1])
    if len(argv) > 2:
        dstparts = splitpath(argv[2])
    else:
        dstparts = srcparts.copy()
        dstparts[2] = '.txt'
    print(joinpath(srcparts))

    with open(joinpath(srcparts), 'rt') as srcfile:
        html = srcfile.read()

    # Extract the article part of the HTML document.
    pat_article = re.compile('.*<article>(.*)</article>.*', re.I|re.S)
    parts = re.split(pat_article, html)
    text = parts[1]

    pats_remove = [
        re.compile('<pre class="(python|console)">.*?</pre>', re.I|re.S),
        re.compile('<table>(.*?)</table>', re.I|re.S),
        re.compile('<div class="[^"]*expr[^"]*">.*', re.I),
        re.compile('</?[^>]+>'),
        re.compile(r'[\t ]+$', re.M),
    ]

    for pat in pats_remove:
        text = re.sub(pat, '', text)

    pats_replace = [
        (re.compile('&larr;', re.I), '<-'),
        (re.compile('&nbsp;', re.I), ' '),
        (re.compile('&mdash;', re.I), '--'),
        (re.compile('&minus;', re.I), '-'),
        (re.compile('&ndash;', re.I), '-'),
        (re.compile('&pi;', re.I), 'PI'),
        (re.compile('&rarr;', re.I), '->'),
        (re.compile('&lt;', re.I), '<'),
        (re.compile('&gt;', re.I), '>'),
        (re.compile('&amp;', re.I), '&'),
        (re.compile('&[^;]+;'), ''),
    ]

    for pat, repl in pats_replace:
        text = re.sub(pat, repl, text)

    with open(joinpath(dstparts), 'wt') as dstfile:
        dstfile.write(text)


def splitpath(pathname):
    parts = []
    temp = os.path.split(pathname)
    parts.append(temp[0])
    temp = os.path.splitext(temp[1])
    parts.extend(temp)
    return parts


def joinpath(pathparts):
    dirname = pathparts[0]
    basename = pathparts[1]
    suffix = pathparts[2]
    if len(dirname) == 0:
        joined = f"{basename}{suffix}"
    else:
        joined = f"{dirname}/{basename}{suffix}"
    return joined


if __name__ == "__main__":
    main(sys.argv)
