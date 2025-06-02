
MENU_OPTIONS = {
    1: "Show Todos",
    2: "Add",
    3: "Update",
    4: "Remove",
    5: "Toggle done",
    0: "Exit"
}

def show_menu(title="Default TodoList Title"):
    divider="-------------------------"
    divLen=int((len(divider)-len(title))/2)
    print(f"{divider[0:divLen]} {title} {divider[0:divLen]}")
    
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
        
    print(f"{divider}\n\n\n")
        
    action=int(input("Enter the number (eg. 1..5) : "))
    # validation
    if action.isdigit()?None:exit(1)
    #switch(action) | not used in python instead in py^3.10+ we have match,funfact it does not require explicit break
    match(action):
        case 0:
            print("exit")
            exit(1)
        case 1:
            
            print(action)
        case 2:
            print(action)
        case 3:
            print(action)
        case 4:
            print(action)
        case _:
            print("Invalid input")
    
    

    
# storage 
todo_list=[]
def show_todos(todos):
    if not todos:
        print("Your todo list is empty!")
        return
    
    print("\nYour Todo List:")
    print("-------------------")
    for idx, todo in enumerate(todos, start=1):
        status = "Done" if todo.get("done", False) else "Pending"
        print(f"{idx}. {todo['task']}  [{status}]")
    print("-------------------\n")
#add,update remove
def add():
    # take input , append to list and give confirmation
    str=string(input("\nEnter the To-Do\n:"))
    # possibly some validations
    todolist.append(str)

def update():
    # take index of todo which user wants to update , take input and update
    nIndex=int(input("\nEnter the Index of To-Do you want to update\n:"))
    # validations
    if( nIndex.isdigit() && nIndex>0 && nIndex <=len(todolist))?None:exit(1)
    
    str=string(input("\Enter the updated To-Do\n:"))
    todolist[nIndex-1]=str
    
# toggle done or undone

    
def start():
    while(True):
        show_menu()

start()