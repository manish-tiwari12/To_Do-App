#  To Do List...

def task():
    tasks = []
    print("---- Welcome The Management App ----")

    totel_task = int(input("Enter How Meny Task You Want To Add..!"))
    for i in range(1, totel_task + 1):
        task_name = input(f"Enter Task {i} = ")
        tasks.append(task_name)

    print(f"Today's Task are\n {tasks}")

    while True:
        oparation = int(input("Enter\n 1-Add\n2-Update\n3-delete\n4-view\n5-exite/stop"))

        if oparation == 1:
            add = input("Enter Task To Want Add..!")
            tasks.append(add)
            print(f"Task{add} has been successfully Add..!")

        elif oparation == 2:
            upadted_val = input('Enter Your Task To Update')
            if upadted_val in tasks:
                up = input("Enter New Task = ")
                ind = tasks.index(upadted_val)
                tasks[ind] = up
                print(f"Updated Taks {up}")
        elif oparation == 3:
            delete_task = input("Enter Your Task To delete..!")
            if delete_task in tasks:
                ind = tasks.index(delete_task)
                del tasks[ind]
                print(f"Task {delete_task} Has been deleted")
        elif oparation == 4:
            print(f"Totel Task is : \n{tasks}")

        elif oparation == 5:
            print("Program Is Closing...")
            break
        
        else:
            print("Involid input")

task()
