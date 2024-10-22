import json
import os
from datetime import datetime

# A file for storing tasks:
TASK_FILE = "tasks.json"

# A function to load tasks from a JSON file:
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# A function to save tasks to a JSON file:
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# A function for displaying a welcome message:
def display_welcome():
    try:
        cons_width = os.get_terminal_size().columns
    except OSError:
        cons_width = 80  # Default width if terminal size can't be determined
    welcome_msg = "--- Welcome to the To-Do List Application ---"
    instruction_msg = "Manage your tasks efficiently!"

    print("\n" + welcome_msg.center(cons_width))
    print(instruction_msg.center(cons_width) + "\n")

# A function to add a new task:
def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter task priority (low, medium, high): ").strip().lower()
    due_date = input("Enter due date (YYYY-MM-DD): ")

    # Validate the due date format
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    task = {
        "name": name,
        "priority": priority,
        "due_date": str(due_date),
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{name}' added successfully!")

# A function to view all tasks:
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n" + " " * 5 + "Task List:")
    for index, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        print(f"{index + 1}. {task['name']} (Priority: {task['priority']}, Due: {task['due_date']}, Status: {status})")

# A function to update an existing task:
def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the task to update: ")) - 1
            if 0 <= index < len(tasks):
                print("Leave the field empty if you do not want to update it.")
                name = input(f"Enter new name (current: {tasks[index]['name']}): ") or tasks[index]['name']
                priority = input(f"Enter new priority (current: {tasks[index]['priority']}): ") or tasks[index]['priority']
                due_date = input(f"Enter new due date (current: {tasks[index]['due_date']}): ") or tasks[index]['due_date']

                # Validate the new due date format
                if due_date:
                    try:
                        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                        return
                
                tasks[index] = {
                    "name": name,
                    "priority": priority,
                    "due_date": str(due_date),
                    "completed": tasks[index]["completed"]  # Keep the completed status the same
                }
                save_tasks(tasks)
                print(f"Task '{name}' updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# A function to mark a task as completed:
def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                save_tasks(tasks)
                print(f"Task '{tasks[index]['name']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to view completed tasks
def view_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task["completed"]]
    
    if not completed_tasks:
        print("No completed tasks found.")
        return
    
    print("\nCompleted Tasks:")
    for index, task in enumerate(completed_tasks):
        print(f"{index + 1}. {task['name']} (Priority: {task['priority']}, Due: {task['due_date']})")

# Function to unmark a completed task
def unmark_task_completed(tasks):
    view_completed_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the completed task to unmark: ")) - 1
            completed_tasks = [task for task in tasks if task["completed"]]
            if 0 <= index < len(completed_tasks):
                completed_tasks[index]["completed"] = False
                save_tasks(tasks)
                print(f"Task '{completed_tasks[index]['name']}' has been unmarked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                save_tasks(tasks)
                print(f"Task '{deleted_task['name']}' has been deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function to run the To-Do List Application
def run_todo_list():
    tasks = load_tasks()
    display_welcome()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. View Completed Tasks")
        print("6. Unmark Completed Task")
        print("7. Delete Task")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            view_completed_tasks(tasks)
        elif choice == "6":
            unmark_task_completed(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            print("Thank you for using the To-Do List. GOODBYE !!!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the To-Do List application
if __name__ == "__main__":
    run_todo_list()
