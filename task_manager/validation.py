from datetime import datetime


def validate_task_title(title):
    """Validate that a task title is not blank."""
    if not isinstance(title, str) or not title.strip():
        print("Invalid title. Please enter a non-empty task title.")
        return False
    return True


def validate_task_description(description):
    """Validate that a task description is not blank."""
    if not isinstance(description, str) or not description.strip():
        print("Invalid description. Please enter a non-empty task description.")
        return False
    return True


def validate_due_date(due_date):
    """Validate that the due date uses YYYY-MM-DD format."""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except (TypeError, ValueError):
        print("Invalid due date. Please use the format YYYY-MM-DD.")
        return False
    return True

