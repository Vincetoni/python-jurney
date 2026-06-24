import os

FILE_NAME = "todo"

def load_tasks():
    """Loads tasks from the text file. Creates the file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Overwrites the text file with the updated list of tasks."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_tasks(tasks):
    """Displays the current to-do list."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    print("\n--- Your To-Do List ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    while True:
        tasks = load_tasks()
       
        print("\n=== To-Do CLI ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
       
        choice = input("Choose an option (1-4): ").strip()
       
        if choice == "1":
            show_tasks(tasks)
           
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"Added: '{new_task}'")
            else:
                print("Task cannot be empty.")
               
        elif choice == "3":
            show_tasks(tasks)
            if not tasks:
                continue
               
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Deleted: '{removed}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
               
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()