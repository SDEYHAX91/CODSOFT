Tasks = []          # TASK LIST

while True:
    ## MENU
    print('''                                                            
To-Do List App:         
    
Menu:
[Select (1-5) only]

1. Add Task.
2. View Task(s).
3. Mark Task as Done.
4. Remove Task.
5. Update Task.
6. Exit.        
            ''')

    try:
        x = int(input("Enter a number (1-5 only): "))                   # INPUT MENU NO.

        match x:

            case 1:                                                     # ADDING TASK
                task = input("Enter task: ").strip()                            
                if task not in Tasks:
                    Tasks.append(task)
                    print("Task added successfully.\n")
                elif task == '' or ' ' or '\n' or '\t':
                    print("Task cannot be empty.\n")
                else:
                    print("Task already in the To-do list.\n")

            case 2:                                                     # VIEWING ALL TASKS
                if not Tasks:
                    print("No task available.\n")
                else:                                                    
                    print("== List of all Tasks ==\n")
                    for i in range(len(Tasks)):
                        print(f"{i+1}. {Tasks[i]}")

            case 3:                                                     # MARKING TASK AS DONE
                if not Tasks:
                    print("No task available.\n")
                    continue
                try:
                    t = int(input("Enter task number to be marked as done: "))
                    if Tasks[t-1][-2:] == ' ✅':
                        print("Task is already marked as done.\n")
                    else:    
                        Tasks[t-1] = Tasks[t-1] + " ✅"    
                        print("Given task is marked as done successfully.\n")   
                except:
                    print("Invalid task number.\n")     

            case 4:                                                         # REMOVING TASK
                if not Tasks:
                    print("No tasks available.\n")
                    continue
                try:
                    r = int(input("Enter task number to be removed: "))     
                    removed = Tasks.pop(r-1)
                    print(f"Task : {removed} has been removed successfully.\n")
                except:
                    print("Invalid task number.\n")

            case 5:                                                         # UPDATING TASK
                if not Tasks:
                    print("No tasks available.\n")
                    continue
                try:
                    u = int(input("Enter task number to be updated: "))
                    updated = input("Enter updated task: ")
                    Tasks[u-1] = updated
                except:
                    print("Invalid task number.\n")

            case 6:                                                         # EXIT FROM THE APP
                print("Exiting To-Do List App. Goodbye!")
                break                                                

            case __:
                print("Invalid number, Please Try again.\n")

    except:
        print("Please enter a valid number.\n")

