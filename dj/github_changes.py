from github import Github
import os
from datetime import datetime as dt, timedelta
import datetime
from collections import defaultdict
import requests

# Set up your GitHub token
# Note: You can create a token at https://github.com/settings/tokens

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REPO_NAME = 'Fellow-Consulting-AG/Fellow2KV'

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Get the date 3 months ago
three_months_ago = dt.now() - timedelta(days=90)

# Fetch commits since 3 months ago
commits = repo.get_commits(since=three_months_ago)

author_changes = {}

for commit in commits:
    if commit.author:
        author_name = commit.author.name
        if author_name in author_changes:
            author_changes[author_name].append(commit)
        else:
            author_changes[author_name] = [commit]

with open('report.txt', 'w') as report:
    for author, author_commits in author_changes.items():
        report.write(f"{author}: {len(author_commits)} commits\n")
        author_image_url = author_commits[0].author.avatar_url
        report.write(f"Author image: {author_image_url}\n")

        weekly_commits = {}

        for commit in author_commits:
            commit_week = commit.commit.committer.date.strftime("%Y-W%U")
            if commit_week in weekly_commits:
                weekly_commits[commit_week].append(commit)
            else:
                weekly_commits[commit_week] = [commit]

        for week, week_commits in weekly_commits.items():
            report.write(f"Week {week}:\n")
            for commit in week_commits:
                report.write(f"- {commit.sha}: {commit.commit.message}\n")

                # Get commit diff
                headers = {"Authorization": f"token {GITHUB_TOKEN}"}
                url = f"https://api.github.com/repos/{REPO_NAME}/commits/{commit.sha}"
                response = requests.get(url, headers=headers)
                commit_info = response.json()
                commit_diff = commit_info['files'][0]['patch']
                diff_lines = commit_diff.splitlines()

                if len(diff_lines) > 2:
                    report.write(f"Code changes:\n{commit_diff}\n")
                else:
                    report.write("Code changes: Less than 2 lines, skipping.\n")