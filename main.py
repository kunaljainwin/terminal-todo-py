
menu = {
    1: "Show Todos",
    2: "Add",
    3: "Update",
    4: "Remove",
    5: "Toggle done",
    0: "Exit"
}

def ShowMenu(title="Default TodoList Title"):
    divider="-------------------------"
    divLen=int((len(divider)-len(title))/2)
    print(f"{divider[0:divLen]} {title} {divider[0:divLen]}")
    
    for key, value in menu.items():
        print(f"{key}. {value}")
        
    print(f"{divider}\n\n\n")
        
    action=int(input("Enter the number (eg. 1..5) : "))
    
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
todolist=[]
#add,update remove
# toggle done or undone

    
def start():
    while(True):
        ShowMenu()

start()