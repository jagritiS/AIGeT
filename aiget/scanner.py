import os
import re

def scan_todos(root_dir):
    todos = []
    pattern = re.compile(r"# TODO: (.*)")  # Extend for other languages
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):  # You can extend to .js, .java, etc.
                file_path = os.path.join(subdir, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f.readlines(), start=1):
                        match = pattern.search(line)
                        if match:
                            todos.append({
                                "text": match.group(1).strip(),
                                "file": file_path,
                                "line": i
                            })
    return todos
