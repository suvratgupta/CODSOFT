import os

# Function to display the to-do list
def display_list(tasks):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for better presentation
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks):
            status_marker = "✅" if task[1] else "⬜"
            print(f"{index+1}. {status_marker} {task[0]}")
    else:
        print("\nYour to-do list is currently empty.")

# Function to add a task
def add_task(tasks):
    new_task = input("\nEnter a new task to add: ")
    tasks.append([new_task, False])
    print(f"\nTask '{new_task}' added successfully!")

# Function to mark a task as complete
def mark_complete(tasks):
    display_list(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the number of the task to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1][1] = True
                print(f"\nTask '{tasks[task_number - 1][0]}' marked as completed!")
            else:
                print("\nInvalid task number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

# Function to remove a task
def remove_task(tasks):
    display_list(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                print(f"\nTask '{task_number}' removed successfully!")
            else:
                print("\nInvalid task number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

def main():
    tasks = []  
    # Create an empty list to store tasks
    while True:
        display_list(tasks)
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_complete(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\nExiting To-Do List...")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
