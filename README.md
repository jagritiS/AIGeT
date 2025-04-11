# AIGeT - Auto Issue Generator for TODO Comments

**AIGeT** automatically scans your code for `TODO` comments and creates GitHub issues from them.

## Features
- Automatically converts `TODO` comments into GitHub issues.
- Integrates easily as a GitHub Action.

## Setup Instructions

1. **Fork this repository** and clone it to your local machine.
2. **Add the AIGeT Action** to your repository:
   - Copy the `aiget-action.yml` from the `.github/workflows/` folder in this repository.
   - Paste it into your own `.github/workflows/` folder in your GitHub repository.

3. **Create a Personal Access Token (PAT)**:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens) and create a new token with **repo** and **workflow** permissions.
   - Save the token securely.

4. **Add the Token as a Secret**:
   - Go to your repository settings.
   - Under **Secrets** > **Actions**, add a new secret with the name `AIGET_GITHUB_TOKEN` and paste your token in the value field.

5. **Add TODO Comments in Your Code**:
   - In any Python file, add a `TODO` comment, for example:
     ```python
     # TODO: Refactor this function
     ```

6. **Push the Changes**:
   - Once the workflow and secret are set up, push your changes to GitHub.
   - The GitHub Action will automatically run and generate issues based on the TODO comments.

## Example
```python
# TODO: Refactor this function to improve performance
