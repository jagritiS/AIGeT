import os
from github import Github

# Initialize GitHub client with token from secrets
token = os.getenv("AIGET_GITHUB_TOKEN")
if not token:
    raise Exception("AIGET_GITHUB_TOKEN not found in environment variables")
g = Github(token)

def sync_issues(todos):
    repo_name = os.getenv("GITHUB_REPOSITORY")  # Example: "jagritiS/AIGeT"
    if not repo_name:
        raise Exception("GITHUB_REPOSITORY not found in environment variables")

    repo = g.get_repo(repo_name)

    # Get existing open issues with AIGeT label
    existing = {issue.title for issue in repo.get_issues(state="open", labels=["AIGeT"])}

    for todo in todos:
        title = f"[AIGeT] TODO: {todo['text']}"
        body = f"📄 `{todo['file']}`, line {todo['line']}"
        label = todo.get("label", "todo")

        if title in existing:
            continue  # Skip if issue already exists

        repo.create_issue(title=title, body=body, labels=[label, "AIGeT"])
