import openai, os
import fnmatch
import time
import mistune

from retry import retry
from openai.error import RateLimitError, APIError




def is_valid_markdown(text):
    try:
        # Attempt to parse the text as Markdown
        mistune.markdown(text)
        return True
    except Exception:
        return False


def find_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, "*.md"):
                file = os.path.join(root, basename)
                file_base, _ = os.path.splitext(file)
                

                




                with open(file, "r") as f:
                    text = f.read()

                f.close()

                new_text = text.replace("Polydocs GmbH", "FellowPro AG")

                

                with open(file, "w") as f:
                    f.write(new_text)

                f.close()

                

file = "/Users/daniel/dev/docapp-docs/docs/en/doc2/keyboard.md"
directory_path = "/Users/daniel/dev/docapp-docs/docs/en/doc2/"
find_md_files(directory_path)

