import os
import fnmatch
import time
import mistune

import markdown


def is_valid_markdown(text):
    try:
        # Attempt to parse the text as Markdown
        mistune.markdown(text)
        return True
    except Exception:
        return False


def find_md_files(directory):
    html = ""
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, "*.md"):
                file = os.path.join(root, basename)
                file_base, _ = os.path.splitext(file)
                print(file)
                with open(file, "r") as f:
                    text = f.read()
                    html += markdown.markdown(text)
    with open('all.html', 'w') as f:
        f.write(html)                


directory_path = "/Users/daniel/dev/docapp-docs/docs/en/docbits/"
find_md_files(directory_path)

