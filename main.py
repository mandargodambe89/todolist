	

import os
import json
from datetime import datetime

# File where tasks will be saved
TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({"task": title, "completed": False, "completed_at": None})
        save_tasks(tasks)
        print(f"✔️ Task '{title}' added!")
    else:
        print("❌ Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for index, item in enumerate(tasks, start=1):
        status = "✅ [Done]" if item["completed"] else "❌ [Pending]"
        timestamp = f" (Completed: {item['completed_at']})" if item["completed_at"] else ""
        print(f"{index}. {status} {item['task']}{timestamp}")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter the number of the task to complete: "))
        if 1 <= choice <= len(tasks):
            target_task = tasks[choice - 1]
            if not target_task["completed"]:
                target_task["completed"] = True
                # Generate timestamp
                target_task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"🎉 Task marked as complete at {target_task['completed_at']}!")
            else:
                print("This task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TERMUX TO-DO APP ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
		
