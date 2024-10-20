# To-do list management
todo_list = []

def show_tasks():
    if len(todo_list) == 0:
        print("Your to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    print()

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task():
    show_tasks()
    if len(todo_list) > 0:
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def mark_task_complete():
    show_tasks()
    if len(todo_list) > 0:
        try:
            task_num = int(input("Enter the number of the task you completed: "))
            completed_task = todo_list[task_num - 1]
            print(f"Task '{completed_task}' marked as complete!")
            todo_list[task_num - 1] = completed_task + " (completed)"
        except (ValueError, IndexError):
            print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Show To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_task_complete()
        elif choice == '5':
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice, please select from 1 to 5.")

# Run the To-Do List application
main()
