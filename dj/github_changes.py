from github import Github, GithubException
import os
from datetime import datetime as dt, timedelta
import datetime
from collections import defaultdict
import requests
import time
import json
# Set up your GitHub token
# Note: You can create a token at https://github.com/settings/tokens

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

Short_Name  = "Fellow2KV"

if not os.path.exists(Short_Name):
    os.makedirs(Short_Name)
    
REPO_NAME = 'Fellow-Consulting-AG/Fellow2KV'
# Set the maximum number of retries
MAX_RETRIES = 3

# Initialize the retry counter
retry_count = 0


g = Github(GITHUB_TOKEN)


while retry_count < MAX_RETRIES:
    try:
        repo = g.get_repo(REPO_NAME)
        break
    except GithubException.RateLimitExceededException as e:
        retry_count += 1
        reset_time = int(e.headers.get("X-RateLimit-Reset"))
        reset_time_utc = datetime.utcfromtimestamp(reset_time).strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"Rate limit exceeded. Will reset at {reset_time_utc}. Retrying in 60 seconds... (retry {retry_count}/{MAX_RETRIES})")
        time.sleep(60)


# Get the date 3 months ago
three_months_ago = dt.now() - timedelta(days=90)

# Set the maximum number of retries
MAX_RETRIES = 3

# Initialize the retry counter
retry_count = 0

# Fetch commits with retries
while retry_count < MAX_RETRIES:
    try:
        commits = repo.get_commits(since=three_months_ago)
        break
    except Github.GithubException.RateLimitExceededException as e:
        retry_count += 1
        reset_time = int(e.headers.get('X-RateLimit-Reset'))
        reset_time_utc = datetime.utcfromtimestamp(reset_time).strftime('%Y-%m-%d %H:%M:%S UTC')
        print(f"Rate limit exceeded. Will reset at {reset_time_utc}. Retrying in 60 seconds... (retry {retry_count}/{MAX_RETRIES})")
        time.sleep(60)  # Wait for 60 seconds before retrying

if retry_count == MAX_RETRIES:
    print("Max retries reached. Exiting...")
    exit(1)

author_changes = {}

for commit in commits:
    if commit.author:
        author_name = commit.author.name
        if author_name in author_changes:
            author_changes[author_name].append(commit)
        else:
            author_changes[author_name] = [commit]

for author, author_commits in author_changes.items():
    author_image_url = author_commits[0].author.avatar_url

    weekly_commits = {}

    for commit in author_commits:
        commit_week = commit.commit.committer.date.strftime("%Y-W%U")
        if commit_week in weekly_commits:
            weekly_commits[commit_week].append(commit)
        else:
            weekly_commits[commit_week] = [commit]
   

    for week, week_commits in weekly_commits.items():
        print (f" We are looking to Week: {week}")
        if author is not None:
            report_filename = f"report_{author.replace(' ', '_')}_{week}.json"
        else:
            report_filename = f"report_unknown_author_{week}.json"
        
        report_data = {
            "author": author,
            "week": week,
            "total_commits": len(week_commits),
            "author_image": author_image_url,
            "commits": []
        }
        
        for commit in week_commits:
            commit_info = {
                "sha": commit.sha,
                "message": commit.commit.message,
                "code_changes": "",
            }
            # Get commit diff
            headers = {"Authorization": f"token {GITHUB_TOKEN}"}
            url = f"https://api.github.com/repos/{REPO_NAME}/commits/{commit.sha}"
            try:
                response = requests.get(url, headers=headers)
                commit_data = response.json()
                if "files" in commit_data and len(commit_data['files']) > 0 and "patch" in commit_data['files'][0]:
                    commit_diff = commit_data['files'][0]['patch']
                    commit_info["code_changes"] = commit_diff
            except IndexError:
                print(f"Could not retrieve commit diff for commit {commit.sha}. Continuing to the next commit...")

            report_data["commits"].append(commit_info)

        with open(os.path.join(Short_Name, report_filename), 'w') as report:
            json.dump(report_data, report, indent=4)