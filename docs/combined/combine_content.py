import os
import re
import subprocess
import webbrowser

chrome_pathname = "C:/Program Files/Google/Chrome/Application/chrome.exe"
edge_pathname = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

zip_pathname = "combined/cse111_content.zip"
html_pathname = "combined/cse111_content.html"
prepare_pathname = "combined/cse111_prepare_content.html"


site_filenames = [
    "site/main.js",
    "site/scope.js",
    "site/reset.css",
    "site/style.css",
    "site/hljs/LICENSE",
    "site/hljs/README.md",
    "site/hljs/highlight.min.js",
    "site/hljs/vscode.css",

    "site/icons/collapsed.webp",
    "site/icons/expanded.webp",
    "site/icons/logo.webp",
    "site/icons/reference.svg",
    "site/icons/tutorial.svg",
    "site/icons/video.svg",
]

image_filenames = [
    "lesson03/call.svg",
    "lesson03/call_graph_check.svg",
    "lesson03/call_graph_key.svg",
    "lesson03/call_graph_prepare.svg",
    "lesson03/call_graph_prove.svg",
    "lesson03/call_graph_teach.svg",
    "lesson03/cylinder.svg",
    "lesson04/call_graph_prove.svg",
    "lesson04/call_graph_teach.svg",
    "lesson04/call_graph_teach_stretch.svg",
    "lesson05/call_graph_check.svg",
    "lesson05/call_graph_teach.svg",
    "lesson06/call_graph_prove.svg",
    "lesson07/call_graph_prove.svg",
    "lesson08/call_graph_prove.svg",

    "lesson01/dark_green_run.webp",
    "lesson01/install.webp",
    "lesson01/in_file_dir.webp",
    "lesson01/light_green_run.webp",
    "lesson01/settings.webp",
    "lesson04/cone.webp",
    "lesson05/install_pytest.webp",
    "lesson05/open_terminal.webp",
    "lesson05/terminal.webp",
    "lesson05/upgrade_pip.webp",
    "lesson06/step_into.webp",
    "lesson06/step_over.webp",

    "lesson05/water_distrib_system.png"
]

text_filenames = [
    "lesson09/plants.txt",
    "lesson09/provinces.txt",
    "lesson10/scores.txt",
    "lesson11/phone_numbers.txt",
    "lesson11/proposal.txt",
    "lesson12wwb/report_1.txt",
    "lesson13wwb/report_2.txt",
    "lesson14/reflection.txt",

    "lesson09/dentists.csv",
    "lesson09/hymns.csv",
    "lesson09/products.csv",
    "lesson09/request.csv",
    "lesson09/students.csv",
    "lesson10/accidents.csv",
    "lesson10/fuel_usage.csv",
    "lesson11/pupils.csv"
]

content_filenames = [
    "combined/title.html",
    "index.html",
    "overview/syllabus.html",

    "lesson01/dev_env.html",
    "lesson01/sample.py",
    "lesson01/prepare.html",
    "lesson01/check.html",
    "lesson01/check_solution.py",
    "lesson01/teach.html",
    "lesson01/teach_solution.py",
    "lesson01/prove.html",

    "lesson02/prepare.html",
    "lesson02/check.html",
    "lesson02/check_solution.py",
    "lesson02/teach.html",
    "lesson02/teach_solution.py",
    "lesson02/teach_stretch.py",
    "lesson02/prove.html",

    "lesson03/prepare.html",
    "lesson03/check.html",
    "lesson03/check_solution.py",
    "lesson03/teach.html",
    "lesson03/teach_solution.py",
    "lesson03/prove.html",

    "lesson04/prepare.html",
    "lesson04/check.html",
    "lesson04/check_solution.py",
    "lesson04/teach.html",
    "lesson04/teach_solution.py",
    "lesson04/teach_stretch.py",
    "lesson04/prove.html",

    "lesson05/prepare.html",
    "lesson05/check.html",
    "lesson05/words.py",
    "lesson05/test_words.py",
    "lesson05/check_solution.py",
    "lesson05/teach.html",
    "lesson05/names.py",
    "lesson05/teach_solution.py",
    "lesson05/address.py",
    "lesson05/teach_stretch.py",
    "lesson05/prove.html",

    "lesson06/prepare.html",
    "lesson06/check.html",
    "lesson06/teach.html",
    "lesson06/teach_solution.py",
    "lesson06/prove.html",

    "lesson07/prepare.html",
    "lesson07/check.html",
    "lesson07/pass_args.py",
    "lesson07/teach.html",
    "lesson07/test_random_numbers.py",
    "lesson07/teach_solution.py",
    "lesson07/prove.html",
    "lesson07/test_chemistry_1.py",

    "lesson08/prepare.html",
    "lesson08/check.html",
    "lesson08/vehicles.py",
    "lesson08/check_solution.py",
    "lesson08/teach.html",
    "lesson08/family_history.py",
    "lesson08/teach_solution.py",
    "lesson08/prove.html",
    "lesson08/formula.py",
    "lesson08/test_chemistry_2.py",

    "lesson09/prepare.html",
    "lesson09/write_text.html",
    "lesson09/check.html",
    "lesson09/provinces.txt",
    "lesson09/check_solution.py",
    "lesson09/file_setup.html",
    "lesson09/teach.html",
    "lesson09/students.csv",
    "lesson09/test_students.py",
    "lesson09/teach_solution.py",
    "lesson09/prove.html",
    "lesson09/products.csv",
    "lesson09/request.csv",
    "lesson09/test_products.py",

    "lesson10/prepare.html",
    "lesson10/fuel_usage.csv",
    "lesson10/check.html",
    "lesson10/get_line.py",
    "lesson10/accidents.csv",
    "lesson10/teach.html",
    "lesson10/accidents.py",
    "lesson10/teach_solution.py",
    "lesson10/prove.html",

    "lesson11/prepare.html",
    "lesson11/check.html",
    "lesson11/phone_numbers.txt",
    "lesson11/add_area_code.py",
    "lesson11/test_add_area_code.py",
    "lesson11/check_solution.py",
    "lesson11/teach.html",
    "lesson11/pupils.csv",
    "lesson11/pupils.py",
    "lesson11/teach_solution.py",
    "lesson11/prove.html",
    "lesson11/proposal.txt",

    "lesson12/prepare.html",
    "lesson12/check.html",
    "lesson12/check_solution.py",
    "lesson12/teach.html",
    "lesson12/heart_rate.py",
    "lesson12/number_entry.py",
    "lesson12/teach_solution.py",
    "lesson12/prove.html",

    "lesson13/prove.html",

    "lesson14/prepare.html"
]

prepare_filenames = [
    "combined/title.html",
    "index.html",
    "overview/syllabus.html",

    "lesson01/prepare.html",
    "lesson02/prepare.html",
    "lesson03/prepare.html",
    "lesson04/prepare.html",
    "lesson05/prepare.html",
    "lesson06/prepare.html",
    "lesson07/prepare.html",
    "lesson08/prepare.html",
    "lesson09/prepare.html",
    "lesson10/prepare.html",
    "lesson11/prepare.html",
    "lesson12/prepare.html",

    "lesson14/prepare.html"
]


def main():
    cwd = os.getcwd()
    print(cwd)
    if cwd.endswith("combined"):
        os.chdir("..")
    #zip_content(zip_pathname)
    #combine_html(html_pathname, content_filenames)
    combine_html(prepare_pathname, prepare_filenames)


def zip_content(outname):
    if os.path.exists(outname):
        os.remove(outname)

    command = ["zip", "-qo9", outname]
    command.extend(content_filenames)
    command.extend(site_filenames)
    command.extend(image_filenames)
    command.extend(text_filenames)
    print(command)
    subprocess.run(command)

    #command = ["zip", "-qo9", outname]
    #command.extend(content_filenames)
    #print(command)
    #subprocess.run(command)


def combine_html(outname, innames):
    with open(outname, "wt", encoding="utf-8", newline="\n") as outfile:
        write_head(outfile)
        for original in innames:
            #print(original, flush=True)
            with open(original, "rt", encoding="utf-8") as infile:
                if original.endswith(".py") \
                        or original.endswith(".csv") \
                        or original.endswith(".txt"):
                    write_code(outfile, infile, original)
                else:
                    write_html(outfile, infile, original)
        write_foot(outfile)
    open_html(outname)


def open_html(outname):
    pathname = os.path.join(os.getcwd(), outname)
    url = "file:///" + re.sub(r"\\", "/", pathname)
    print(url)

    # Open the combined HTML file in Microsoft edge because it seems to
    # be the only browser that can correctly produce a PDF from the
    # combined HTML file.
    webbrowser.register('edge', EdgeBrowser)
    webbrowser.get('edge').open_new_tab(url)


def write_code(outfile, infile, original):
    class_names = {".py":"python", ".csv":"csv", ".txt":"text"}
    lastdot = original.rindex(".")
    suffix = original[lastdot:]
    class_name = class_names[suffix]
    outfile.write('<section>\n' +
        f'<h1>{original}</h1>\n' +
        '<div class="pre solution"><pre class="linenums"></pre>\n' +
        f'<pre class="{class_name}">')
    sep = ""
    for text in infile:
        text = text.rstrip()
        if len(text) > 71:
            text = text[:71]
        outfile.write(sep)
        outfile.write(entity_from_char(text))
        sep = '\n'
    outfile.write('</pre>\n' +
        '</div>\n' +
        '</section>\n')


def write_html(outfile, infile, original):
    srcvalpat = re.compile(r'^(.*)src="([^"]+)"(.*)$')
    srcprotopat = re.compile(r'src="https?[^"]+"')
    idpat = re.compile(r'id="([^"]+)"')
    datarefpat = re.compile(r'data-ref="([^"]+)"')
    dataforpat = re.compile(r'data-for="([^"]+)"')

    prefix = re.sub("lesson([0-9][0-9])", r"l\1", original)
    prefix = prefix.replace(".html", "")
    prefix = prefix.replace("/", "_")
    #print(prefix)

    folder = os.path.dirname(original)
    #filename = os.path.basename(original)
    print(original)

    # Skip all lines up to and including <main>.
    for text in infile:
        if text.startswith("<main"):
            break

    outfile.write('\n' +
        '<section>\n')
    # Add all lines up to but excluding </main>.
    for text in infile:
        if text.startswith("</main"):
            break
        if srcvalpat.search(text) and not srcprotopat.search(text):
            relpath = srcvalpat.sub(r"\2", text).strip()
            relpath = os.path.join(folder, relpath)
            abspath = os.path.abspath(relpath)
            common = os.path.commonpath([os.getcwd(), abspath])
            relpath = os.path.relpath(abspath, common)
            relpath = relpath.replace("\\", "/")
            #print(relpath)
            repl = f'\\1src="../{relpath}"\\3'
            #print(repl)
            text = srcvalpat.sub(repl, text)
        if idpat.search(text):
            text = idpat.sub(f'id="{prefix}_\\1"', text)
        if datarefpat.search(text):
            text = datarefpat.sub(f'data-ref="{prefix}_\\1"', text)
        if dataforpat.search(text):
            text = dataforpat.sub(f'data-for="{prefix}_\\1"', text)
        outfile.write(text)
    outfile.write('</section>\n')


def write_head(outfile):
    outfile.write(
'''<!DOCTYPE html>
<!-- Copyright 2019, Brigham Young University - Idaho. All rights reserved. -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script defer src="../site/main.js"></script>
    <script defer src="../site/hljs/highlight.min.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans&family=Source+Code+Profamily=Crimson+Pro&display=swap">
    <link rel="stylesheet" href="../site/reset.css">
    <link rel="stylesheet" href="../site/style.css">
    <link rel="stylesheet" href="../site/hljs/vscode.css">
    <link rel="icon" type="image/webp" href="../site/icons/logo.webp">
    <title>CSE 111</title>
</head>

<body>
<main>''')


def write_foot(outfile):
    outfile.write(
'''</main>
</body>
</html>
''')


def entity_from_char(code):
    return code.replace('&', '&amp;') \
                .replace('<', '&lt;') \
                .replace('>', '&gt;')


"""
def make_filenames(original):
    localpath = f"{docs_base}/{original}".replace("/", "\\")
    if original.endswith(".py") \
        or original.endswith(".csv") \
        or original.endswith(".txt"):
        remotepath = f"{repo_base}/overview/solution.html?file={original}"
    else:
        remotepath = f"{repo_base}/{original}"

    basename = original.replace(".", "_") + ".pdf"
    savepath = f"{out_path}/{basename}".replace("/", "\\")
    return localpath, remotepath, savepath
"""


class EdgeBrowser:
    def __init__(self):
        self.name = 'edge'

    def open(self, url, new=0, autoraise=True):
        # These command line arguments of /n and /t don't do anything.
        # They're either not the correct arguments or they don't work
        # because nearly all edge command-line flags only take effect if
        # they are passed on the command line when all Edge instances
        # are closed.
        if new == 2:
            args = [edge_pathname, '/n', url]
        elif new == 1:
            args = [edge_pathname, '/t', url]
        else:  # new == 0
            args = [edge_pathname, url]
        subprocess.Popen(args)

    def open_new(self, url):
        self.open(url, 1)

    def open_new_tab(self, url):
        self.open(url, 2)


if __name__ == "__main__":
    main()
