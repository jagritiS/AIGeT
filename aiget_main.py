from aiget.scanner import scan_todos
from aiget.ai_classifier import classify_todo
from aiget.issue_manager import sync_issues

def main():
    print("************************* Scanning for TODOs *********************************")
    todos = scan_todos(".")

    print(f" !!!****Found {len(todos)} TODOs. Classifying ****!!!")
    classified_todos = [
        {
            **todo,
            "label": classify_todo(todo["text"])
        }
        for todo in todos
    ]

    print(" !!!!***** Syncing with GitHub Issues *****!!!!")
    sync_issues(classified_todos)
    print("******************** Done ***********************")

if __name__ == "__main__":
    main()
