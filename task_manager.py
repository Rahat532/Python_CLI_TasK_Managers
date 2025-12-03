import os 
import json
import csv

# lets create file to store tasks
file_name = "tasks.txt"
def load_tasks():
    """Load tasks from the file."""
    tasks = {}
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 5:
                    tasks_id,tasks_title,tasks_status,tasks_priority,tasks_deadline = parts
                    tasks[int(tasks_id)]={'title':tasks_title,'status':tasks_status,'priority':tasks_priority,'deadline':tasks_deadline}
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(file_name,'w') as file:
        for tasks_id,task in tasks.items():
            file.write(f"{tasks_id}|{task['title']}|{task['status']}|{task['priority']}|{task['deadline']}\n") 

# Function to add a new task
def add_task(tasks, title):
    title= input("Enter task title: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {'title': title, 'status': 'incomplete', 'priority': priority, 'deadline': deadline}
    print(f"Task '{title}' added with ID {task_id}.")
    
# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}, Priority: {task['priority']}, Deadline: {task['deadline']}")

# Function to mark a task as complete
def complete_task(tasks):
    task_id =int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]['status'] = 'complete'
        print(f"Task ID {task_id} marked as complete.")
    else:
        print(f"Task ID {task_id} not found.")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Deleted task: {deleted_task['title']}")
        print(f"Task ID {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")

# Function to export tasks as JSON
def export_json(tasks):
    filename = input("Enter filename for JSON export (without extension): ") + ".json"
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks exported to {filename}")

# Function to export tasks as CSV
def export_csv(tasks):
    filename = input("Enter filename for CSV export (without extension): ") + ".csv"
    if not tasks:
        print("No tasks to export.")
        return
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Title', 'Status', 'Priority', 'Deadline'])
        for task_id, task in tasks.items():
            writer.writerow([task_id, task['title'], task['status'], task['priority'], task['deadline']])
    print(f"Tasks exported to {filename}")

# Function to export tasks menu
def export_tasks(tasks):
    print("\nExport Options:")
    print("1. Export as JSON")
    print("2. Export as CSV")
    export_choice = input("Choose format: ")
    
    if export_choice == '1':
        export_json(tasks)
    elif export_choice == '2':
        export_csv(tasks)
    else:
        print("Invalid choice.")

# Main function to run the task manager
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Export Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks, title="")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            export_tasks(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
            
if __name__ == "__main__":
        main()