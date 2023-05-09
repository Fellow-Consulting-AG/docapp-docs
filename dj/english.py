import openai, os
import fnmatch
import time
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")


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
                file1 = os.path.join(root, basename)

                with open(file1, "r") as f:
                    text = f.read()

                f.close()

                print("Waiting for 1 minute...")
                time.sleep(60)  # Wait for 60 seconds (1 minute)

                MODEL = "gpt-3.5-turbo"
                response = openai.ChatCompletion.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": f"You are SEO and Marketing Expert please return only a Code. Use this Text: {text}"},
                        {"role": "user", "content": "Analyze the given markdown and improve it for SEO and Marketing. If Alt Images are missing Add alt images in the Markdown. <div class='video-container'> or other code oder javascript do not remove it. in the header please set it on today. Please return only a Code."},
                    ],
                    temperature=0,
                )

                response = response["choices"][0]["message"]["content"]
                file_base, file_extension = os.path.splitext(file)
                

                split_response = response.split("```")

                if len(split_response) < 3:
                    print("Error: No code returned")

                    
                else:
                    changes_made = split_response[2]
                    code = split_response[1]

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
                        print (f"No change for {file1}")

file = "/Users/daniel/dev/docapp-docs/docs/en/doc2/keyboard.md"
directory_path = "/Users/daniel/dev/docapp-docs/docs/en/"
find_md_files(directory_path)

