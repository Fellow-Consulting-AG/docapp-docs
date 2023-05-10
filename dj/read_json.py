import openai, os
import fnmatch
import time
import mistune

from retry import retry
from openai.error import RateLimitError, APIError, APIConnectionError

import json


openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"

import spacy

from spacy.cli import download




def trim_text(text):

    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    

    doc = nlp(text)
    if len(doc) > 2000:
        doc = doc[:2000]
        trimmed_text = str(doc)
        return trimmed_text
    else:
        return text

@retry((RateLimitError, APIError,APIConnectionError), tries=5, delay=90, backoff=2)
def generate_response(text):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": f"You are an API and can only response with a JSON Use this JSON: {text}"},
            {"role": "user", "content": "please analyse the code_change and write a code_change_description what was done here second add a code smell range 1-10 as code_smell_rating and a github label as github_labels Return only with a JSON Response"},
        ],
        temperature=0,
    )
    return response

@retry((RateLimitError, APIError,APIConnectionError), tries=5, delay=90, backoff=2)
def generate_response2(text):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": f"You are an API and can only response with a JSON Use this Text: {text}"},
            {"role": "user", "content": "please add summary what the developer was doing for the week as summary second make a marketing summary as marketing_summary Return only with a JSON Response "},
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
    output_dir = "/Users/daniel/dev/docapp-docs/dj/output"  # Create a separate directory to save the updated files
    os.makedirs(output_dir, exist_ok=True) 
    for root, dirs, files in os.walk(directory):
        for basename in files:
            print (f"basename: {basename}")
            if fnmatch.fnmatch(basename, "*.json"):
                file = os.path.join(root, basename)
                print (f" file: {file}")
                file_base, _ = os.path.splitext(file)
                

                with open(file, "r") as f:
                    json_data = json.load(f)
                

                for commit in json_data["commits"]:

                    text = commit["code_changes"]

                    text = trim_text(text)
                
                    print("Waiting for 1 seconds...")
                    time.sleep(1)  # Wait for 60 seconds (1 minute)

                    MODEL = "gpt-3.5-turbo"
                    try:
                        response_full = generate_response(text)
                        # Process the response as needed
                    except RateLimitError:
                        print("Failed after multiple retries due to rate limit error.")

                    response = response_full["choices"][0]["message"]["content"]

                    
                    try:
                        # Try to parse response as JSON
                        new_json = json.loads(response)
                    except json.JSONDecodeError:
                        # If response cannot be parsed as JSON, break the loop
                        print("Response is not valid JSON. Skipping this commit.")
                        continue

                
                    file_base, file_extension = os.path.splitext(file)

                    # Update the code_changes value in the commit
                    for c in json_data["commits"]:
                        if c["sha"] == commit["sha"]:
                            c["code_changes"] = commit["code_changes"]
                            c["code_change_description"] = new_json["code_change_description"]
                            c["code_smell_rating"] = new_json["code_smell_rating"]
                            c["github_labels"] = new_json["github_labels"]
                            
                            break
                
                print ("Writing to file")
                # Write the updated JSON data back to disk
                output_file = os.path.join(output_dir, "New_" + basename)
                print (f"output_file: {output_file}")
                with open(output_file, "w") as f:
                    json.dump(json_data, f)

                f.close()

                # Last Step 

                with open(output_file, "r") as f:
                    json_data = json.load(f)
                
                f.close()
                

                test = ""


                for commit in json_data["commits"]:
                    if "code_change_description" in commit:
                        test = test + " " + commit['code_change_description']
                    
                
                if len(text)>20:
                
                    print("Waiting for 1 seconds...")
                    time.sleep(1)  # Wait for 60 seconds (1 minute)

                    MODEL = "gpt-3.5-turbo"
                    try:
                        response = generate_response2(text)
                            # Process the response as needed
                    except RateLimitError:
                        print("Failed after multiple retries due to rate limit error.")

                    response = response["choices"][0]["message"]["content"]

                    try:
                        # Try to parse response as JSON
                        new_json = json.loads(response)
                    except json.JSONDecodeError:
                        # If response cannot be parsed as JSON, break the loop
                        print("Response is not valid JSON. Skipping this commit.")
                        continue

                    if "summary" in new_json:

                        json_data["summary"] = new_json["summary"]
                        json_data["marketing_summary"] = new_json["marketing_summary"]

                        
                        # Write the updated JSON data back to disk
                        output_file = os.path.join(output_dir, "New2_" + basename)
                        print (f"output_file: {output_file}")
                        with open(output_file, "w") as f:
                            json.dump(json_data, f)

                        f.close()


#file = "/Users/daniel/dev/docapp-docs/docs/en/doc2/keyboard.md"
directory_path = "/Users/daniel/dev/docapp-docs/dj/Fellow2KV2"
find_md_files(directory_path)

