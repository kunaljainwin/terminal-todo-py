![image](https://github.com/user-attachments/assets/763509e7-7237-4f51-9bb8-84ea003dbcd4)

# terminal-todo-py

A simple, terminal-based To-Do list manager written in Python. Manage your daily tasks from the command line with a clean menu interface, persistent storage, and a beginner-friendly structure.

---

## 🚀 Features

- 📋 Add, update, remove tasks
- ✅ Toggle task status between Done and Pending
- 🧠 Persistent storage using `todos.json`
- 🧼 Input validation and structured CLI menu
- 🧱 Easily extensible for new features

---

## 🛠️ Planned Enhancements

- ⏰ Add due dates to tasks
- ⚡ Assign priorities (low, medium, high)
- 🎨 Color-coded terminal output for Done/Pending
- 🗄️ Replace JSON storage with SQLite database

---

## 🐍 Requirements

- Python 3.7+
- (Optional) `colorama` for colored terminal output:
  ```bash
  pip install colorama


git clone https://github.com/kunaljainwin/terminal-todo-py.git
cd terminal-todo-py

python main.py

main.py           # Main application script
todos.json        # Auto-generated persistent storage (JSON)
README.md         # Project documentation


----------------- My TodoList -----------------
1. Show Todos
2. Add
3. Update
4. Remove
5. Toggle done
0. Exit
-----------------------------------------------

Enter the number (e.g. 1..5): 2
Enter the To-Do: Buy groceries
Added todo: Buy groceries


🧠 Why This Project?
This project is designed to help you:

Practice core Python skills (functions, lists, file I/O)

Learn basic CLI application patterns

Understand persistence using JSON

Prep for working with databases and larger apps
