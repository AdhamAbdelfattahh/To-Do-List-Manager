def display_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nTo-Do List is empty.")

def main():
    tasks = []
    
    while True:
        print("\nSelect an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Exiting the To-Do List Manager.")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
