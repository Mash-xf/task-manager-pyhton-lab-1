from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):

    try:
        if not validate_task_title(title):
            return

        if not validate_task_description(description):
            return

        if not validate_due_date(due_date):
            return

    except ValueError:
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):

    if index < 0 or index >= len(tasks):
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):

    for i, task in enumerate(tasks, start=1):
        if not task["completed"]:
            print(f"\nTask {i}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")


def calculate_progress(tasks=tasks):

    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100