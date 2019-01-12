#import libraries
import sqlite3
import sys

#Create a Database to store data

connection = sqlite3.connect('sqlite3_mydata.db')

#create an object that will be used by all the command like INSERT, SELECT.
cursor = connection.cursor()

#Create a table 

cursor.execute('CREATE TABLE tasks ( id INTEGER PRIMARY KEY, task TEXT)')

#Add, edit,view and delete data from the table


class myToDo:
    def message(self):
        print("Here is my To Do Lists \n ")

# this function will be used to enter the choices for the task we choose to do

    def choices(self):
        enter_choices = 0
        while(enter_choices!=5):
            enter_choices = input("\n 1. Add a task \n 2. View a task. \n 3. edit the task.\n 4. Delete a task. \n 5. Exit the program \n ")
            if enter_choices == 1:
                task = raw_input("Enter the task to add into the list \n")
                cursor.execute('INSERT INTO tasks(task) VALUES(?)', (task,))
                connection.commit()
                raw_input("Press the Enter key to continue")
            elif enter_choices == 2:
                print("Here is the complete view of your todo list \n")
                cursor.execute('SELECT * FROM tasks') #it will select all the data from the tasks table
                row = cursor.fetchone() #this is a method to print all the data present in the table
                while row is not None:
                    id = [0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone() # check for the data again
                raw_input("Press the Enter key to continue . \n")
            elif enter_choices == 3:
                print("Enter the id to edit task list  \n")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = [0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone()
                number = input('\n')
                task = raw_input('\n Edit any task from the list \n')
                query = "UPDATE tasks SET task = " + "'"+task+"'"+"WHERE id = "+number
                cursor.execute(query)
                raw_input("Press the Enter key to continue . \n")
            elif enter_choices == 4:
                print("Enter the id to delete task list  \n")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = [0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone()
                number = input('\n')
                #task = raw_input('\n Delete any task from the list \n')
                query = "DELETE FROM tasks WHERE id = "+number
                cursor.execute(query)
                raw_input("Press the Enter key to continue . \n")
            else:
                print("End the program")
                sys.exit()
end = myToDo()
end.message()
end.choices()






#import libraries
import sqlite3
import sys

#Create a Database to store data

connection = sqlite3.connect('sqlite3_mydata.db')

#create an object that will be used by all the command like INSERT, SELECT.
cursor = connection.cursor()

#Create a table 

cursor.execute('CREATE TABLE tasks ( id INTEGER PRIMARY KEY, task TEXT)')

#Add, edit,view and delete data from the table


class myToDo:
    def message(self):
        print("Here is my To Do Lists")

# this function will be used to enter the choices for the task we choose to do

    def choices(self):
        enter_choices = 0
        while(enter_choices!=5):
            enter_choices = input("\n 1. Add a task \n 2. View a task. \n 3. edit the task.\n 4. Delete a task. \n 5. Exit the program \n ")
            if enter_choices == 1:
                task = raw_input("Enter the task to add into the list \n")
                cursor.execute('INSERT INTO tasks(task) VALUES(?)', (task,))
                connection.commit()
                raw_input("Press the Enter key to continue")
            elif enter_choices == 2:
                print("Here is the complete view of your todo list \n")
                cursor.execute('SELECT * FROM tasks') #it will select all the data from the tasks table
                row = cursor.fetchone() #this is a method to print all the data present in the table
                while row is not None:
                    id = [0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone() # check for the data again
                raw_input("Press the Enter key to continue . \n")
            elif enter_choices == 3:
                print("Enter the id to edit task list  \n")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = [0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone()
                number = input('\n')
                task = raw_input('\n Edit any task from the list \n')
                query = "UPDATE tasks SET task = " + "'"+task+"'"+"WHERE id = "+number
                cursor.execute(query)
                raw_input("Press the Enter key to continue")
            elif enter_choices == 4:
                print("Enter the id to delete task list  \n")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = [0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone()
                number = input('\n')
                #task = raw_input('\n Delete any task from the list \n')
                query = "DELETE FROM tasks WHERE id = "+number
                cursor.execute(query)
                raw_input("Press the Enter key to continue")
            else enter_choices == 5:
                print("End the program")
                sys.exit()
end = myToDo()
end.message()
end.choices()






