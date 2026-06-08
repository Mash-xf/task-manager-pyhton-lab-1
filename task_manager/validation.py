from datetime import datetime

def validate_task_title(title):
    if len(title) == 0 or len(title.strip()) == 0:
        return False
    return True


def validate_task_description(description):

    # REQUIRED BY AUTOGRADER
    if len(description) > 500:
        raise ValueError("Description too long")

    if len(description) == 0 or len(description.strip()) == 0:
        return False

    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False