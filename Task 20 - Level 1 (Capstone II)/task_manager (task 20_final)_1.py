# Please note that this program is intended to help businesses manage tasks
# assigned to each member. It offers functionality like
# adding users, adding and viewing tasks.

# The below stated functionality is coded into the program, which generates 
# these scenarios where user input is required:
# If the user inputs an invalid entry
# Once the error  is flagged , the user is prompted to re-input their expected data.
# Done via loop
# The user can enter -1 at any time to return to the main menu
# The limitations are however, at login and when the user is already at the main menu.

# The following libraries are imported to increase
# functionality to the program.
import os
from datetime import datetime
import time

# The following variables have been declared to be
# used during the program.
current_path = os.path.dirname(__file__)
delay_menu = 3
delay_login_exit = 1
first_login = True

####### FUNCTIONS #######
# Check the users list and observe if the user enters by looping through
# the username and corresponding password as expected.
# No access should be granted if user inputs incorrect details. Prompt them to retry
def login():
    print("Hi, Welcome to the Task Manager!")
    print("\n To login, please ensure that you enter your user details...\n")

    user_pass = False
    pass_pass = False

    # Keep looping until the user inputs an accepted username
    while not user_pass:
        usern = input("Username: ")
        for x in range(0, len(users)):
            if users[x][0] == usern:
                user_pass = True

                if user_pass:

                    # Continue to generate the loop until the user enters the correct password
                    while not pass_pass:
                        password = input("Password: ")
                        if users[x][1] == password:
                            pass_pass = True

                        if not pass_pass:
                            print("\nPassword incorrect. Please retry.")
        if not user_pass:
            print("\nUsername incorrect. Please retry.")

        # The delay gives the sense of a real feel effect
        else:
            print("Logging in...")
            time.sleep(delay_login_exit)
            print("\nWelcome!")
            print("Please note: Input \"-1\" in order to return to the Main Menu.")
            time.sleep(delay_login_exit+1)
    
    # Return the username to the variable
    return usern

# If the user inputs 'r' after the prompt, the user is allowed to add a new user.
# A username entry is prompted from the user
# password to add. The user must confirm the password.
# If the passwords do not match the user is requested
# to retry. Users can only be registered by the admin.
def reg_user():
    user_unique = False
    verify_pass = False

    # Performs a check to determine if the current user is "admin". If not,
    # restrict access to the function and print not authorised.
    if username == "admin":
        print("\nUser Registration\nPlease enter the new users details")

        # Keep looping until user enters a unique username
        while not user_unique:
            unique = True
            new_user = input("Username:\t\t")

            # Break and return to main menu if the user ever enters "-1"
            if new_user == "-1":
                break
            
            # Prompt the user to input something, otherwise allow them to loop back and let them try again
            elif new_user == "":
                print("\nPlease enter a valid username...\n")
            
            # Check to observe whether there is an exisitng username.
            else:
                for x in range(0, len(users)):
                    if users[x][0] == new_user:
                        print("\nThe username already exists. Please choose a different username.\n")
                        unique = False
                if unique:
                    user_unique = True

        if new_user == "-1":
            pass

        else:
            # Loop until the user correctly confirms the password.
            while not verify_pass:
                new_pass1 = input("Password:\t\t")
                if new_pass1 == "":
                    print("\nPlease enter a valid password.\n")
                elif new_pass1 == "-1":
                    break
                else:
                    new_pass2 = input("Confirm Password:\t")

                    if new_pass2 == "-1":
                        break

                    # Print the new user details and add that user to the file (usernames must match)
                    elif new_pass1 == new_pass2:
                        verify_pass = True
                        user.write(f"\n{new_user}, {new_pass1}")
                        print(f"\nNew user has been added\nUsername:\t{new_user}\nPassword:\t{new_pass1}")

                    else:
                        print("\nPasswords do not match. Please retry.\n")

        # Write both the password & usernames to the appropriate file.\
        verify_pass = False

    else:
        print('\nThe authorisation to register new users has not been granted.')

    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# If the user enters 'a' after the prompt, the user is allowed to add a new task.
# The user is requested to enter the various details and store the task in the text file.
def add_task():
    print("\nAdd Task\nPlease enter the neccessary details for the new task:")
    
    # Create the variables to save the data input from the user.
    info = []
    _info_title_ = ['Username:\t', 'Task Title:\t', 'Description:\t', 'Date Assigned:\t', 'Due Date:\t', 'Completed:\t']
    skip = False

    # Loop through each input and save it in a list.
    for x in range(0, 6):
        while True:
            data = input(f"{_info_title_[x]}")
            
            # It is important to ensure that the user has entered datavthat is valid.
            if data == "":
                print("\nInvalid input. Please try again.\n")
            else:
                info.append(data)
                break
        
        # Break the loop if the user inputs '-1'
        # Update variable 'skip'
        # of the function to return to the main menu.
        if info[x] == "-1":
            skip = True
            break

    # Check if the user wishes to return to the menu.
    if not skip:

        # Write the follwing information to the task to the file.
        task.write(f"\n{info[0]}, {info[1]}, {info[2]}, {info[3]}, {info[4]}, {info[5]}")

        # Confirm the details by printing to the screen.
        print("\nNew task has been added")
        print("----------------------------------------------------")
        print("Username:\t" + info[0])
        print("Task Title:\t" + info[1])
        print("Description:\t" + info[2])
        print("Date Assigned:\t" + info[3])
        print("Due Date:\t" + info[4])
        print("Completed:\t" + info[5])
        print("----------------------------------------------------")

    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# If the user enters 'va' ,the details of all users for all tasks will be printed
def view_all():
    print("\nView All Tasks")

    # Loop through each line of the 'tasks' list and
    # print to the screen.
    for line in tasks:
        print("----------------------------------------------------")
        print("Username:\t" + line[0])
        print("Task Title:\t" + line[1])
        print("Description:\t" + line[2])
        print("Date Assigned:\t" + line[3])
        print("Due Date:\t" + line[4])
        print("Completed:\t" + line[5])
        print("----------------------------------------------------")

    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# Should the user enter 'vm' all the tasks that are affiliated with the user are printed
# The user is requested to choose a task number to edit.
# Once they've inputed a task number, the user is given the option to mark as complete 
# or make edits to the tasks username and due date
def view_mine():
    user_found = False
    my_tasks = []
    print("\nView My Tasks")

    # Loop through all the tasks in the list and add the tasks
    # that are affiliated with the present user to the new variable 'my_tasks'.
    for x in range(0, len(tasks)):
        if username == tasks[x][0]:
            my_tasks.append(tasks[x])
            user_found = True

    # If the programs locates the user, print each task assigned to that
    # user and add a task number to correspond with each task
    if user_found:
        for x in range(0, len(my_tasks)):
            print(f"\nTask {x+1}")
            print("----------------------------------------------------")
            print("Username:\t" + my_tasks[x][0])
            print("Task Title:\t" + my_tasks[x][1])
            print("Description:\t" + my_tasks[x][2])
            print("Date Assigned:\t" + my_tasks[x][3])
            print("Due Date:\t" + my_tasks[x][4])
            print("Completed:\t" + my_tasks[x][5])
            print("----------------------------------------------------")

        # Prompt the user to enter the task that they want to edit
        # Keep looping until the user enters a valid task number or inputs '-1'.
        # to return to the main menu.
        while True:
            # Add a a limitation in the event that the user doesn't enter
            # anything and presses enter. This would return an error
            # Its best to limit the error, and break the loop by returning to the main menu.
            
            try:
                task_num = int(input("Please input the number of the task that you'd like to edit: "))
                if task_num == -1:
                    break

                # Check that the task number is within the available tasks
                # per the file. This is to ensure we don't get any error.
                elif task_num > 0 and task_num <= len(my_tasks):
                    
                    # If the user enters a valid task number, we want to remove
                    # that task from the "tasks" list. This is because we are going
                    # to edit the task using "my_tasks" and then add the newly edited
                    # task back to "tasks" and print the entire list to the tasks.txt
                    # file again. This is easier than trying to edit the individual task
                    # in the "tasks" list.
                    for x in range(0, len(my_tasks)):
                        tasks.remove(my_tasks[x])

                    # Loop until the user enters a valid option
                    while True:
                        print("\nPlease choose an option")
                        print("m - mark task as complete\ne - edit the task")
                        menu_choice = input()

                        # If the user chooses "m", edit the Completed to "Yes".
                        # Not going to check whether it is already "Yes" since
                        # not changing any other variables based on this.
                        if menu_choice == "m":
                            my_tasks[task_num-1][5] = "Yes"
                            print(f"\nTask {task_num} has been marked as complete.")
                            break

                        elif menu_choice == "-1":
                            break

                        # If the user chooses "e", they can edit the Username and Due Date
                        # of the task. However, check if the task has been marked as Completed
                        # and don't allow editing if this is the case.
                        elif menu_choice == "e":
                            if my_tasks[task_num-1][5] == "Yes":
                                print("\nThe task has been completed. Unable to edit.")
                                break
                            else:
                                print("\nPlease enter the new Username and Due Date (leave blank if no change required).")
                                usern = input("Edit Username:\t")
                                due_date = input("Edit Due Date:\t")
                                
                                # Check if the users inputs are not blank. If they
                                # are blank the varibales won't be edited.
                                if usern != "":
                                    my_tasks[task_num-1][0] = usern
                                if due_date != "":
                                    my_tasks[task_num-1][4] = due_date

                                print("\nUpdated details")
                                print("Username:\t" + my_tasks[task_num-1][0])
                                print("Due Date:\t" + my_tasks[task_num-1][4])
                                break
                        
                        # Let the user know if the input is not recognised
                        else:
                            print("\nUnrecognized input.")
                            time.sleep(delay_login_exit)

                    # When the editing is done, move the cursor in the file to the start.
                    # Clear the file of all contents.
                    # Add the newly edited tasks in "my_tasks" to "tasks".
                    # Write all the tasks back to the text file.
                    task.seek(0)
                    task.truncate(0)
                    for x in range(0, len(my_tasks)):
                        tasks.append(my_tasks[x])
                    for x in range(0, len(tasks)):
                        task.write(", ".join(tasks[x]))
                        if x != len(tasks)-1:
                            task.write("\n")
                    
                    break
                
                # Let the user know if the task entered does not exist.
                else:
                    print("\nThe selected task does not exist. Please try again.\n")
            except:
                print("\nNo task number entered. Please try again.\n")
                

    # Let the user know if they have no tasks.
    if not user_found:
        print("No tasks found for current user.")

    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)
    
# If the user enters 'ds' and the user happens to be
# the "admin", various statistics are shown to the user on screen
# and the corresponding reports that are generated in text files.
def display_statistics():
    
    # Check if the users is "admin" before executing the function.
    if username == "admin":
        
        # Call the function to generate reports for each call as the information
        # could have undergone some change since the last function call.
        generate_reports()

        # Open the generated report files.
        task_over_r = open(os.path.join(current_path, "task_overview.txt"), "r+")
        user_over_r = open(os.path.join(current_path, "user_overview.txt"), "r+")

        print(f"\nOpening task_overview.txt in {delay_menu} seconds...\n")
        time.sleep(delay_menu)

        # Due to the difference in the way the terminal and text documents
        # handle the Tab (\t) delimter, the format appears the require a few
        # adjustments so that the info that is read from the files and ultimately printed, match.
        # In this case, we are removing all \t delimters from the file, and adding new
        # \t delimiters based on the terminals needs.
        for line in task_over_r:
            if "Total" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))
        
        print(f"\nOpening user_overview.txt in {delay_menu} seconds...\n")
        time.sleep(delay_menu)

        for line in user_over_r:
            if "User:" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t\t"))
            elif "User Tasks" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

    # If the user is not "admin" let them know they are not authorised
    # to use this function.
    else:
        print("\nYou do not have the required authorisation to view statistics.\n")

    print(f"Returning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# This is the program loop which runs until the program is exited.
while True:

    # Open the text files and read the contents into a list variable.
    # Strip the next line delimeters from the end of the lines.
    user = open(os.path.join(current_path, "user.txt"), "r+")
    users = user.readlines()
    users = [x.strip().split(", ") for x in users]

    task = open(os.path.join(current_path, "tasks.txt"), "r+")
    tasks = task.readlines()
    tasks = [x.strip().split(", ") for x in tasks]

    # Check if the user has logged in yet and if not,
    # call the login function and save the returned
    # current user in "username".
    if first_login:
        username = login()
        first_login = False    
    
    # Print the menu options and request the user to enter
    # a selection from the menu. Print different options
    # for admin and a normal user.
    if username == "admin":
        print("\nPlease select one of the following options:")
        print("r - register user\na - add task\nva - view all tasks\nvm - view my tasks\nds - display statistics\ne - exit")
        menu = input("")
    else:
        print("\nPlease select one of the following options:")
        print("a - add task\nva - view all tasks\nvm - view my tasks\ne - exit")
        menu = input("")

    # Call the applicable function based on the users menu input.
    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "ds":
        display_statistics()

    # If the user inputs 'e' the main loop is stopped and
    # the program exits.
    elif menu == "e":
        print("\nExiting...")
        time.sleep(delay_login_exit)
        break

    # If the input the user has entered is not recognised the user is
    # notified and the loop starts again.
    else:
        print("\nInvalid input. Please retry.")
        time.sleep(delay_login_exit)

    # The files are closed to ensure all new data is written.
    user.close()
    task.close()
