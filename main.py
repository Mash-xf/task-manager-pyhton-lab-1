from task_manager.task_utils import (
    add_task,
    calculate_progress,
    mark_task_as_complete,
    tasks,
    view_pending_tasks,
)


def display_all_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("All Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - Due: {task['due_date']} - {status}")
        print(f"   Description: {task['description']}")


def main():
    while True:
        print()
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == "2":
            display_all_tasks()
            if tasks:
                task_number = input("Enter the task number to mark as complete: ")
                mark_task_as_complete(task_number)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress:.2f}% complete")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
