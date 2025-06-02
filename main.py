
import json
import os

DATA_FILE = "todos.json"

# Colors for Text
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as f:# with keeps this file open for this scope only
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Corrupted data file. Starting fresh.")
    else:
        print("This file does not exist")
    
    return []
    
def save_todos():
    if todo_list:
        try:
            with open(DATA_FILE,'w') as f:
                json.dump(todo_list,f,indent=2)
        except (OSError, TypeError) as e:
            print(f"Failed to save todos: {e}")

MENU_OPTIONS = {
    1: "Show Todos",
    2: "Add",
    3: "Update",
    4: "Remove",
    5: "Toggle done",
    0: "Exit"
}

def show_menu(title="My TodoList"):
    divider=f"{RESET}-------------------------"
    divLen=int((len(divider)-len(title)-2)/2)
    print(f"\n\n{divider[0:divLen]} {title} {divider[0:divLen]}")
    
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
        
    print(f"{divider}\n\n")
        
    action = get_user_choice()
    #switch(action) | not used in python instead in py^3.10+ we have match,funfact it does not require explicit break
    match(action):
        case 0:
            save_todos()
            print("Exiting safely... Goodbye!")
            exit(0)
        case 1:
            show_todos()
        case 2:
            add()
        case 3:
            update()
        case 4:
            remove()
        case 5:
            toggle_done()
        case _:
            print("Invalid input")
            
    save_todos()
    
def get_user_choice()->int:
    while True:
        choice = input("Enter the number (e.g. 1..5): ").strip()
        if choice.isdigit():
            choice_int = int(choice)
            if choice_int in MENU_OPTIONS:
                return choice_int
        print("Invalid input, please enter a valid menu number.")
    
# storage 
todo_list=[]
def show_todos():
    if not todo_list:
        print("Your todo list is empty!")
        return
    
    print("\nYour Todo List:")
    print("-------------------")
    for idx, todo in enumerate(todo_list, start=1):
        status = f"{GREEN}Done{RESET}" if todo.get("done", False) else f"{RED}Pending{RESET}"
        print(f"{idx}. {todo['task']}  [{status}]")
    print("-------------------\n")
#add,update remove
def add():
    task = input("Enter the To-Do: ").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        print(f"Added todo: {task}\n")
    else:
        print("Empty task not added.\n")

def update():
    # validations
    if not todo_list:
        print("Todo list is empty! Nothing to update.\n")
        return
    show_todos()
     # take index of todo which user wants to update , take input and update
    idx = input("Enter the index of the To-Do you want to update: ").strip()
    if idx.isdigit():
        idx = int(idx)
        if 1 <= idx <= len(todo_list):
            new_task = input("Enter the updated To-Do: ").strip()
            if new_task:
                todo_list[idx - 1]['task'] = new_task
                print("To-Do updated.\n")
                return
            else:
                print("Empty input. Update cancelled.\n")
                return
    print("Invalid index.\n")
    
    
def remove():
    if not todo_list:
        print("Todo list is empty! Nothing to remove.\n")
        return
    show_todos()
    idx = input("Enter the index of the To-Do you want to remove: ").strip()
    if idx.isdigit():
        idx = int(idx)
        if 1 <= idx <= len(todo_list):
            removed = todo_list.pop(idx - 1)
            print(f"Removed To-Do: {removed['task']}\n")
            return
    print("Invalid index.\n")
# toggle done or undone

def toggle_done():
    if not todo_list:
        print("Todo list is empty! Nothing to toggle.\n")
        return
    show_todos()
    idx = input("Enter the index of the To-Do to toggle done/undone: ").strip()
    if idx.isdigit():
        idx = int(idx)
        if 1 <= idx <= len(todo_list):
            todo_list[idx - 1]['done'] = not todo_list[idx - 1]['done']
            status = "Done" if todo_list[idx - 1]['done'] else "Pending"
            print(f"To-Do marked as {status}.\n")
            return
    print("Invalid index.\n")
    

def start():
    global todo_list
    todo_list = load_todos()
    while(True):
        show_menu()

start()
