# Task Manager CLI

A command-line task management application built with Python that allows you to create, manage, and export tasks with priorities and deadlines.

## Features

- **Add Tasks** - Create new tasks with title, priority level, and deadline
- **View Tasks** - Display all tasks with their details
- **Complete Tasks** - Mark tasks as complete
- **Delete Tasks** - Remove tasks from your list
- **Export Tasks** - Export tasks to JSON or CSV format
- **Persistent Storage** - Tasks are saved to a text file and persist between sessions

## Requirements

- Python 3.x

## Installation

1. Clone or download the project
2. No additional dependencies required (uses only Python standard library)

## Usage

Run the application:

```bash
python task_manager.py
```

### Menu Options

1. **Add Task** - Create a new task
   - Enter task title
   - Choose priority: `high`, `medium`, or `low`
   - Enter deadline in `YYYY-MM-DD` format

2. **View Tasks** - Display all tasks with their details:
   - Task ID
   - Title
   - Status (incomplete/complete)
   - Priority
   - Deadline

3. **Complete Task** - Mark a task as complete by entering its ID

4. **Delete Task** - Remove a task by entering its ID

5. **Export Tasks** - Export your tasks in:
   - **JSON format** - For integration with other applications
   - **CSV format** - For use in spreadsheet applications

6. **Exit** - Save and close the application

## File Format

Tasks are stored in `tasks.txt` with the following format:

```
ID|Title|Status|Priority|Deadline
```

Example:
```
1|Buy groceries|incomplete|high|2025-12-10
2|Complete project|complete|medium|2025-12-15
```

## Export Formats

### JSON Export
Tasks are exported as a JSON object with task IDs as keys:
```json
{
    "1": {
        "title": "Buy groceries",
        "status": "incomplete",
        "priority": "high",
        "deadline": "2025-12-10"
    }
}
```

### CSV Export
Tasks are exported in CSV format with headers:
```
ID,Title,Status,Priority,Deadline
1,Buy groceries,incomplete,high,2025-12-10
```

## Notes

- Task IDs are automatically assigned
- Status values: `incomplete` or `complete`
- Priority levels: `high`, `medium`, `low`
- Deadline format: `YYYY-MM-DD`

## Author

Created as part of the AI Mastery Bootcamp Command Line Project
