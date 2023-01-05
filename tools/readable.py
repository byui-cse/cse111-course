import os
import os.path as path
import re
import sys
import readability


def main(argv):
    argv.pop(0)

    if len(argv) == 0:
        argv = ["."]

    if len(argv) == 2 and path.isfile(argv[0]) and path.isfile(argv[1]):
        srcpath = argv[0]
        dstpath = argv[1]
        measure = measure_file(srcpath, dstpath)
        print(measure, srcpath)
    else:
        measures = []
        for srcpath in argv:
            if path.isdir(srcpath):
                measures.extend(process_dir(srcpath))
            else:
                measures.append(process_dir(srcpath))

        for measure in sorted(measures, key=lambda elem: elem[0], reverse=True):
            print(measure)


def process_dir(dirpath):
    measures = []
    for root, dirnames, filenames in os.walk(dirpath):
        for filename in filenames:
            suffix = path.splitext(filename)[1]
            if suffix == '.html':
                srcpath = path.join(root, filename)
                measures.append(process_file(srcpath))
    return measures


def process_file(srcpath, dstpath=None):
    if dstpath is None:
        parts = path.split(srcpath)
        dirname = parts[0]
        filename = parts[1]
        basename = path.splitext(filename)[0]
        dstpath = path.join(dirname, f"{basename}.txt")
    return measure_file(srcpath, dstpath), srcpath


patterns = [
    # Extract the article part of the HTML document.
    (re.compile('.*<article>(.*)</article>.*', re.I|re.S), r'\1'),

    # Remove all python and console preformatted content.
    (re.compile('<pre class="(python|console)">.*?</pre>', re.I|re.S), ''),

    # Remove all tables.
    (re.compile('<table>(.*?)</table>', re.I|re.S), ' \u00b6 '),

    (re.compile('<h[1-6]>', re.I), ' \u00b6 '),
    (re.compile('<li>', re.I), ' \u00b6 '),
    (re.compile('<p>', re.I), ' \u00b6 '),

    # Remove all mathematical expressions.
    (re.compile('<div class="[^"]*expr[^"]*">.*', re.I), ''),

    # Remove all remaing tags.
    (re.compile('</?[^>]+>'), ''),

    # HTML entities
    (re.compile('&larr;', re.I), ' <- '),
    (re.compile('&nbsp;', re.I), ' '),
    (re.compile('&mdash;', re.I), ' -- '),
    (re.compile('&minus;', re.I), ' - '),
    (re.compile('&ndash;', re.I), ' - '),
    (re.compile('&pi;', re.I), 'PI'),
    (re.compile('&rarr;', re.I), ' -> '),
    (re.compile('&lt;', re.I), ' < '),
    (re.compile('&gt;', re.I), ' > '),
    (re.compile('&amp;', re.I), ' & '),
    (re.compile('&[^;]+;'), ' '),

    # Tokenize the text so that the readability module can process it.
    # Convert all multiple blank lines to a single paragraph symbol.
    (re.compile(r'(\r?\n){2,}'), ' \u00b6 '),

    # Remove all tab and newline characters.
    (re.compile(r'\s+'), ' '),

    # Insert a space before and a newline after each [:;.?!].
    (re.compile('[:;.?!]'), r' \g<0>\n'),

    # Insert a space before each comma.
    (re.compile(','), r' \g<0>'),

    # Insert a space before and after each [_"()[]{}].
    (re.compile('[-"()[\]{}_]'), r' \g<0> '),

    # Clean up extra spaces.
    (re.compile(' {2,}'), ' '),

    # Replace all paragraph symbols with a blank line.
    (re.compile('( ?\u00b6 ?)+'), r'\n\n'),
    (re.compile(r'(\r?\n){3,}'), r'\n\n'),

    # Remove spaces at the start and end of each line.
    (re.compile(r'^[\t ]+', re.M), ''),
    (re.compile(r'[\t ]+$', re.M), ''),
]


def measure_file(srcpath, dstpath):
    print(srcpath)

    with open(srcpath, 'rt', encoding='utf-8') as srcfile:
        text = srcfile.read()

    for pat, repl in patterns:
        text = re.sub(pat, repl, text)

    results = readability.getmeasures(text, lang='en')
    measure = results['readability grades']['GunningFogIndex']

    with open(dstpath, 'wt', encoding='utf-8') as dstfile:
        for key in results:
            print('\t', key, sep='', file=dstfile)
            value = results[key]
            for key2 in value:
                value2 = value[key2]
                if isinstance(value2, float):
                    value2 = round(value2, 2)
                print('\t\t', f"{key2} {value2}", sep='', file=dstfile)
        dstfile.write(text)

    #os.remove(dstpath)
    return round(measure, 2)


if __name__ == "__main__":
    main(sys.argv)
