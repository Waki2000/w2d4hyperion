import os
from datetime import datetime, date
date_format = "%d-%m-%Y"
login = {}
tasks = []
def update_user():
    if not os.path.exists("users.txt"):
        with open("users.txt", "w") as default_file:
            default_file.write("admin;password")

    with open ("users.txt", "r") as file:
        for line in file:
            user_name, password = line.strip().split(";")
            login[user_name] = password 
    #print(login)

def reg_user():
    while True:
        new_username = input("New Username: ")
        if new_username in login.keys(): 
            print("user already exist")
            continue
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        
        if  new_password != confirm_password:
            print("password didn't match, try again")
            continue
        else:
            login[new_username] = new_password
            print ("new username added")
            with open("users.txt", "w") as file:
                for item in login:
                    file.write(f"{item};{login[item]}\n")
                break

def add_task():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass
    task_username = input("Name of person assigned to task: ")
    if task_username not in login.keys():
        print("User does not exist. Please enter complete_tas valid username")
        #continue
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (d-m-Y) : ")
            ntask_due_date = datetime.strptime(task_due_date, date_format) 
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today().strftime(date_format)
    ncurr_date = datetime.strptime(curr_date,date_format)
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    if ntask_due_date>ncurr_date:
        task_completed = "no"
        days_lef = ntask_due_date - ncurr_date
        #print(f"days left: {days_lef}")
    elif ncurr_date>ntask_due_date:
        task_completed = "overdue"
    else:
        task_completed = "yes"
    #print(task_completed)

    task_details = f"{task_username};{task_title};{task_description};{task_due_date};{task_completed}"
    tasks.append(task_details)
    # print(task_details)
    #print(tasks)
    # print(curr_date)

    with open ("tasks.txt", "w") as file:
        for item in tasks:
            file.write(item+"\n")
    print("task has been added")
    

def view_all():
    
    for i, item in enumerate(tasks, 1):
        print(i, item)
        print("-"*20)  
    
def view_mine():
    my_task = []
    other_users_task = []
    for task in tasks:
        #print(task[0])
        line = task.split(";")
        if line[0] == username:
            my_task.append(task)
        else:
            other_users_task.append(task)

    file = open ("tasks.txt", "w")


    for i, item in enumerate(my_task, 1):
        item = item.split(";")
        print(f"{i}. user: {item[0]} \t task_title: {item[1]}  task_description : {item[2]}  due_date: {item[3]}  task_complete?: {item[4]} \n ------------ ")

    
    while True:
        try:
            user_choice = int(input(" (TYPE -1 to exit) or \n select the task you wish TO EDIT *Enter the Task Number:* "))
            if user_choice == -1:
                break
            elif user_choice >0 and user_choice <len(tasks):
                print(f" {username} You have chosen to edit task {user_choice} : {my_task[int(user_choice-1)]}")
                
                while True:
                    my_task[int(user_choice-1)] = my_task[int(user_choice-1)].split(";")
                    menu = input( """please select from the menu if you wish to edit the task:
                    m = to mark the task as complete
                    u = to change username
                    d = to change due date
                    e = exit
                    """).lower()

                    if menu == "m": 
                        if my_task[int(user_choice-1)][4] == "yes":
                            print("this Task has already completed" )

                        elif my_task[int(user_choice-1)][4] == "no" or my_task[int(user_choice-1)][4] == "overdew" :
                                my_task[int(user_choice-1)][4] = "yes"
                                my_task[int(user_choice-1)]= ";".join(my_task[int(user_choice-1)])
                                print("Task completion status updated")
                                break
                        
                    elif menu == "u":
                        new_user_name = input(" please enter the new username : ")
                        if new_user_name not in login.keys():
                            print("User does not exist. Please enter valid username next time")
                            
                        else:
                            my_task[int(user_choice-1)][0] = new_user_name
                            my_task[int(user_choice-1)]= ";".join(my_task[int(user_choice-1)])
                            print("***********username status updated*************")
                        break
                    
                    elif menu == "d":
                        # try:
                        new_date = input (" please enter the new date to be updated : (d-m-Y) : ")
                        #new_date = datetime.strptime(new_date, date_format).date()
                            #my_task[int(user_choice-1)][3]=new_date
                        # except ValueError:
                        #     print("********Invalid datetime format. Please use the format specified*********")

                        # Then get the current date.
                        #today_date = date.today().strftime(date_format)
                        #ntoday_date = datetime.strptime(today_date,date_format)
                        # ''' Add the data to the file task.txt and
                        #     Include 'No' to indicate if the task is complete.'''
                        # if nnew_date>ntoday_date:
                        #     my_task[int(user_choice-1)][4] = "no"
                        #     # days_lef = new_date - today_date
                        #     # print(f"days left: {days_lef}")
                        # elif ntoday_date>nnew_date:
                        #     my_task[int(user_choice-1)][4] = "overdue"
                        # else:
                        #     my_task[int(user_choice-1)][4] = "yes"
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        my_task[int(user_choice-1)][3]=new_date
                        my_task[int(user_choice-1)]= ";".join(my_task[int(user_choice-1)])
                        print("*********date updated*************")
                        break
                    elif menu == "e":
                        print("ba-bye to select a new task or exit")
                        break
                    else:
                        print("Wrong selection please try again")
                #my_task[int(user_choice-1)]= ";".join(my_task[int(user_choice-1)])
                for i in my_task:
                    other_users_task.append(i)
                    #print(my_task)
                    #print(other_users_task)
                for y in other_users_task:
                    file.write(f"{y}\n")
                break     
            else:
                
                print("please try again")
        except: 
           
           print("try a different task")
        
        # for x in range(0, len(my_task)):
        #     other_users_task.append(my_task)
        # for x in range(0, len(other_users_task)):
        #     file.write(", ".join(other_users_task))


def update_task():
      with open ("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())

def menu():

    while True:
            # presenting the menu to the user and 
            # making sure that the user input is converted to lower case.
            print("`~`"*30)

            if username == "admin":
                print(f"\nWelcome to Task manager Dashboard {username} !!\n Please select one of the following options:")
                print("r - register user\n a - add task\n va - view all tasks\n vm - view my tasks\n gr - generate reports\n ds - display statistics\n e - exit")
                menu = input("").lower()
            else:
                print(f"\nWelcome to Task manager Dashboard {username} !!\n Please select one of the following options:")
                print("\n va - view all tasks)\n vm - view my tasks\n e - exit")
                menu = input("").lower()

            print("`~`"*30)
            if menu == 'r':
                reg_user()
            
            elif menu == 'a': 
                add_task()
        
            elif menu == 'va':
                view_all()
                
            elif menu == 'vm':
                view_mine()   
            
            elif menu == 'ds' and username == 'admin':
                display_statistics() 
            
            elif menu == 'gr' and username == 'admin':
                generate_reports()
                
            elif menu == 'e':
                print(f"'Goodbye!!! {username} \n Hope to see you again {username}")
                exit()

            else:
                print(f" Wrong choice {username}, Please Try again")
            print("`~`"*30)
    users.close()
    tasks.close()


def display_statistics():
    '''If the user is an admin they can display statistics about number of users
        and tasks.'''
    num_users = len(login.keys())
    num_tasks = len(tasks)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------") 

def generate_reports():
    task_overview()
    user_overview()

def task_overview():
    
    complete_task=0 
    incomplete_task=0 
    overdue_task=0
    for task in tasks:
        line = task.split(";")
        if line[4] == "yes":
            complete_task += 1
        elif line[4] == "no":
            incomplete_task +=1
        elif line[4] == "overdue":
            overdue_task += 1
    incomplete_task_percentage = round((incomplete_task *100)/len(tasks))
    overdue_task_percentage = round((overdue_task *100)/len(tasks))
    print("-"*50)
    print(f"#1. total number of task generated {(len(tasks))} \n") 
    print(f"#2. total number of completed tasks : task with yes {complete_task}\n")
    print(f"#3. total number of incompleted tasks : tasks with no {incomplete_task}\n")
    print(f"#4. total number of incompleted tasks and+ that are overdue {overdue_task}\n")
    print(f"#5. percentage of task that are incomplete: {incomplete_task_percentage}% \n")
    print(f"#6. percentage of tasks that are overdue: {overdue_task_percentage}% \n")
    print("-"*50)


    with open ("task_overview.txt", "w") as file:
        file.write(
            f"#1. total number of task generated {(len(tasks))}\n"+
            f"#2. total number of completed tasks : task with yes {complete_task}\n"+
            f"#3. total number of incompleted tasks : tasks with no {incomplete_task}\n"+
            f"#4. total number of incompleted tasks and+ that are overdue {overdue_task}\n"+
            f"#5. percentage of task that are incomplete: {incomplete_task_percentage}% \n"+
            f"#6. percentage of tasks that are overdue: {overdue_task_percentage}% \n")

def user_overview():
    
    users = []

    with open ("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip().split(";"))
    #print(tasks)

    with open ("users.txt", "r") as file:
        for line in file:
            user_name, password = line.strip().split(";")
            login[user_name] = password 

    for usernames in login:
        users.append(usernames)

    file = open ("user_overview.txt", "w")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~ User Overview ~~~~~~~~~~~~~~~~~~~~~~\n")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    total_task_by_all_users = 0
    total_task_completed = 0
    total_task_incomplete = 0
    total_task_overdue = 0

    for username in users:
        total_task_by_user = 0
        task_completed = 0
        task_incomplete = 0
        task_overdue = 0
        for job in tasks:
            if username == job[0]:
                total_task_by_user +=1
                total_task_by_all_users+=1
                if username == job[0] and job[4] == 'yes':
                    task_completed +=1
                    total_task_completed+=1
                elif username == job[0] and job[4] == 'no':
                    task_incomplete +=1
                    total_task_incomplete+=1
                elif username == job[0] and job[4] == 'overdue':
                    task_overdue +=1
                    total_task_overdue +=1
        
        print("~"*50)
        print(f"{username} has total {total_task_by_user} tasks")
        print(f"{username} has completed {task_completed} tasks")
        print(f"{username} has {task_incomplete} incomplete tasks")
        print(f"{username} has {task_overdue} overdue tasks")
        print(f"{username} has {round((total_task_by_user)/len(tasks)*100)}% of the total tasks")
        if total_task_by_user>0:
            print(f"{username} has completed {round((task_completed)/total_task_by_user*100)}% tasks and incomplete {round((task_incomplete/total_task_by_user)*100)}% and {round((task_overdue)/total_task_by_user*100)}% overdue tasks")
        else:
            print("no task")
        print("~"*50)
        
        file.write(f"{username} has total {total_task_by_user} tasks\n")
        file.write(f"{username} has completed {task_completed} tasks\n")
        file.write(f"{username} has {task_incomplete} incomplete tasks\n")
        file.write(f"{username} has {task_overdue} overdue tasks\n")
        file.write(f"{username} has {round((total_task_by_user)/len(tasks)*100)}% of the total tasks\n")
        file.write(f"{username} has completed {round((task_completed)/total_task_by_user*100)}% tasks and incomplete {round((task_incomplete/total_task_by_user)*100)}% and {round((task_overdue)/total_task_by_user*100)}% overdue tasks\n")
        file.write(f"{'~'*50}\n")
    file.write(f"All user together has total : {total_task_by_all_users} tasks")
    print(f"All user together has total : {total_task_by_all_users} tasks")

    #file.close()

#~~~~~~~~~~~~~~~~~~~~~~~~
update_task()
update_user()
print("`~`"*30)
while True:
    print("`~``~``~``~``~``~``~``~``~``~``~`Task Manager Login Window `~``~``~``~``~``~``~``~``~``~``~``~`")
    username = input("Username: ")
    password = input("Password: ")
    if username not in login.keys():
        print("User does not exist")
        continue
    elif login[username] != password:
        print("Wrong password")
        continue
    else:
        print(f"Login Successful! Welcome!!! {username}")
        break
menu()

