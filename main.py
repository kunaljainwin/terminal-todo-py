

def ShowMenu(title="Default TodoList Title"):
    print("\n1.Show Todos\n2.Add\n3.Update\n4.Remove\n5.Toggle done\n0.\nExit")
    action=int(input("Enter the number (eg. 1..5)"))
    
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