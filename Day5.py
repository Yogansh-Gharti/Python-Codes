FILE_NAME = "tasks.txt"


def add_task():
    task = input("Enter Task: ")

    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

    print("Task Added Successfully!")


def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No Tasks Found!")
            return

        print("\n===== TASK LIST =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("No Tasks Found!")


def delete_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No Tasks Available!")
            return

        view_tasks()

        task_no = int(input("\nEnter Task Number to Delete: "))

        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)

            print("Task Deleted Successfully!")

        else:
            print("Invalid Task Number!")

    except FileNotFoundError:
        print("No Tasks Found!")


while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
