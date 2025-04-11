from github import Github
import os

def sync_issues(todos):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise Exception("GITHUB_TOKEN not found in env vars")

    repo_name = os.getenv("GITHUB_REPOSITORY")
    g = Github(token)
    repo = g.get_repo(repo_name)

    existing = {issue.title for issue in repo.get_issues(state="open", labels=["AIGeT"])}

    for todo in todos:
        title = f"TODO: {todo['text']}"
        body = f"📄 `{todo['file']}`, line {todo['line']}"
        label = todo.get("label", "todo")

        if title in existing:
            continue

        repo.create_issue(title=title, body=body, labels=[label, "AIGeT"])
