import re
import json
import os
import fnmatch


def extract_images(markdown_text):
    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(image_pattern, markdown_text)

    images = []

    for match in matches:
        alt_text, filename = match
        images.append({"alt_text": alt_text, "filename": filename})

    return json.dumps(images, indent=2)

def seo_optimized_filename(input_string):
    # Convert the string to lowercase
    filename = input_string.lower()

    # Replace any special characters or punctuation with spaces
    filename = re.sub(r'[^a-zA-Z0-9\s]', ' ', filename)

    # Replace multiple spaces with a single space
    filename = re.sub(r'\s+', ' ', filename)

    # Replace spaces with hyphens
    filename = filename.replace(' ', '-')

    # Remove leading or trailing hyphens
    filename = filename.strip('-')

    return filename

def find_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, "*.md"):
                file = os.path.join(root, basename)

                with open(file, "r") as f:
                    text = f.read()

                f.close()

                result = extract_images(text)



                title_pattern = r'title:\s*"([^"]*)"'
                title_match = re.search(title_pattern, text)

                if title_match:
                    title = title_match.group(1)
                    print(title)
                else:
                    print("Title not found.")
                



directory_path = "/Users/daniel/dev/docapp-docs/docs/en/docbits/"
find_md_files(directory_path)