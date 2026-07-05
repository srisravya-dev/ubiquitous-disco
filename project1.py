import os

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                status, task = line.strip().split("|", 1)
                tasks.append({"task": task, "done": status == "1"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            status = "1" if task["done"] else "0"
            file.write(f"{status}|{task['task']}\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

  print("\n------ TO-DO LIST ------")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['task']}")
    print()

# Main program
def main():
    tasks = load_tasks()

  while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

  choice = input("Enter your choice (1-5): ")

  if choice == "1":
            show_tasks(tasks)

  elif choice == "2":
            task = input("Enter new task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")

   elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

  elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Deleted task: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

   elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using the To-Do List App!")
            break

  else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()
