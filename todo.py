import sys

def main():
    while True:
        #Options to display
        print("X-----Options-------")
        print("1. Add a task.")
        print("2. List all tasks.")
        print("3. Exit.")
        print("X-------------------")
        
        #Handling ValueError
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Option Should be a number.")
            continue    
        
        if option == 1:
            add_task()
        elif option == 2:
            list_task()
        elif option == 3:
            sys.exit("Thank You!")
        else:
            print("Invalid Option")
            
tasks = []  


#Append Tasks from user            
def add_task():
    while True:
        task = input("Enter a task / Exit : ").title().strip()
        if task == "Exit":
            break
        elif task == "":
            print("Task should be filled.")
            continue
        else:
            with open("todo.csv", "a") as file:
                file.write(user)        

            
#Lists all tasks            
def list_tasks():
    if not tasks:
        print("Empty tasks.")
    else:
        for task in tasks: 
           print(task)


if __name__ == "__main__":
    main()            