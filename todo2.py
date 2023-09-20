# Creating a list of to-do
todo_list = []

# Displaying the main menu
def main_menu():
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Quit")

# A function which lets you add user task to to-do list
def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

# Create a function that displays the current tasks in the to-do list.
def view_tasks():
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

# Create a function that allows the user to mark a task as complete and remove it from the to-do list.
def mark_task_complete():
    view_tasks()
    task_number = int(input("Enter the number of the task to mark as complete: "))

    if 1 <= task_number <= len(todo_list):
        completed_task = todo_list.pop(task_number - 1)
        print(f"{completed_task} marked as complete!")
    else:
        print("Invalid task number.")

# Use a while loop to continuously display the main menu and handle user input until the user decides to quit the application.
while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
