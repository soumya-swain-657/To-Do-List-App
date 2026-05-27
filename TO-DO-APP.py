FILE_NAME='tasks.txt'

def load_tasks():
    try:
        with open(FILE_NAME,'r') as file:
            tasks=file.readlines()
            return [tasks.Strip() for task in tasks]
        
    except FileNotFoundError:
        return[]
    
def save_tasks(tasks):
    with open(FILE_NAME,'w') as file:
        for task in tasks:
            file.write(task+'\n')
            
def show_tasks(tasks):
    if not tasks:
        print("No task available")
    else:
        print("\n To-do list")
        for i,task in enumerate(tasks,start=1):
            print(f'{i}.{task}')
            
tasks=load_tasks()

while True:
    print("\n =========TO-DO LIST APP==========")
    print("1. View tasks")
    print("2. Add tasks")
    print("3. Update tasks")
    print("4. Delete tasks")
    print("5.Exit")
    
    
    choice=input("Enter your choice")
    if choice =="1":
        show_tasks(tasks)
    elif choice=="2":
        new_tasks=input("Enter new tasks")
        tasks.append(new_tasks)
        save_tasks(tasks)
        print("Task added successfully")

    elif choice =="3":
        show_tasks(tasks)
        task_no=int(input("Enter task number to update"))

        if 1<=task_no<=len(tasks):
            updated_task=input("Enter updates task")
            tasks[task_no-1]=updated_task
            save_tasks(tasks)
            print("Task updated successfully")
        else:
            print("Invalid Task number")

    elif choice=="4":
        show_tasks(tasks)
        task_no=int(input("Enter task number to delete"))
        if 1<=task_no<=len(tasks):
            removed=tasks.pop(task_no-1)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted successfully")
        else:
            print("Invalid Task number")

    elif choice=="5":
        print("Existing To-Do List App")
        break

    else:
        print("Invalid choice! please try again")