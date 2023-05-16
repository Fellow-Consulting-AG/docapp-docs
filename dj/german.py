import openai, os
import fnmatch
import time
import mistune

from retry import retry
from openai.error import RateLimitError, APIError, APIConnectionError




openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"

@retry((RateLimitError, APIError,APIConnectionError), tries=5, delay=90, backoff=2)
def generate_response(text):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": f"You are German SEO and Marketing Expert please return only a Code. Use this Text: {text}"},
            {"role": "user", "content": "Analysieren Sie das gegebene Markdown und verbessern Sie es für SEO und Marketing. Wenn Alt-Bilder fehlen, fügen Sie Alt-Bilder in den Markdown ein. Wenn Sie html oder Code finden, ändern Sie ihn nicht. Übersetzen Sie den Text vom Englischen ins Deutsche im Markdown-Format und erläutern Sie Ihre Änderungen zum Schluss wobei Sie immer mit Changes: <seo_changes > "},
        ],
        temperature=0,
    )
    return response



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
                old_file = file_base + ".old"

                if os.path.exists(old_file):
                    print(f"Skipping {file} because {old_file} already exists.")
                    continue


                with open(file, "r") as f:
                    text = f.read()

                f.close()

                print("Waiting for 10 seconds...")
                time.sleep(1)  # Wait for 60 seconds (1 minute)

                MODEL = "gpt-3.5-turbo"
                try:
                    response = generate_response(text)
                    # Process the response as needed
                except RateLimitError:
                    print("Failed after multiple retries due to rate limit error.")

                response = response["choices"][0]["message"]["content"]
                file_base, file_extension = os.path.splitext(file)
                
                print (f"------ {file} ------")
                print (response)

                split_marker = 'Changes:'
                sections = response.split(split_marker)
                



                if len(sections) < 2:
                    print("Error: No code returned")
                    with open(file_base + ".new", "w") as f:
                            f.write(response)

                    f.close()

                    
                else:
                    main_content = sections[0].strip()
                    seo_and_marketing = split_marker + sections[1].strip()

                    changes_made = seo_and_marketing
                    code = main_content



                    if is_valid_markdown(code):
                        

                        os.rename(file, file_base + ".old")

                        print (code )

                        print (changes_made)

                        with open(file, "w") as f:
                            f.write(code)

                        f.close()



                        with open(file_base + ".txt", "w") as f:
                            f.write(changes_made)

                        f.close()
                    else:
                        print (f"No change for {file}")

#file = "/Users/daniel/dev/docapp-docs/docs/en/doc2/keyboard.md"
directory_path = "/Users/daniel/dev/docapp-docs/docs/de/te2/"
find_md_files(directory_path)

