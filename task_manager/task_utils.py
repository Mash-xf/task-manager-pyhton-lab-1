from task_manager.validation import (
    validate_due_date,
    validate_task_description,
    validate_task_title,
)


tasks = []


def add_task(title, description, due_date, tasks=tasks):
    if not validate_task_title(title):
        return False
    if not validate_task_description(description):
        return False
    if not validate_due_date(due_date):
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return True


def mark_task_as_complete(index, tasks=tasks):
    try:
        task_index = int(index) - 1
    except ValueError:
        print("Invalid task number. Please enter a number.")
        return False

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number. Please choose a task from the list.")
        return False

    tasks[task_index]["completed"] = True
    print("Task marked as complete!")
    return True


def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    for index, task in enumerate(tasks, start=1):
        if not task["completed"]:
            pending_tasks.append((index, task))

    if not pending_tasks:
        print("No pending tasks.")
        return []

    print("Pending Tasks:")
    for index, task in pending_tasks:
        print(f"{index}. {task['title']} - Due: {task['due_date']}")
        print(f"   Description: {task['description']}")

    return pending_tasks


def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0
    else:
        completed_count = sum(1 for task in tasks if task["completed"])
        progress = (completed_count / len(tasks)) * 100

    return progress

