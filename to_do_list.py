def to_do_list():
    tasks = []

    while True:
        print("1. Add task")
        print("2. Remove tasks")
        print("3. Show tasks")
        print("4. Quit")
        choice = int(input("Enter a choice: "))

        match choice:

            case 1:
                task = input("Enter a new task: ")
                tasks.append(task)
            case 2:
                task = input("Enter a task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                else:
                    print("Task not found")
            case 3:
                print("Tasks: ")
                tasks = [print("- " + task) for task in tasks]
            case 4:
                print("Bye!")
                break
            case _:
                print("Choice not found!")

to_do_list()