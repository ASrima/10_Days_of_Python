#import librarires
import sqlite3 # database library
import sys

#Database to store data

connection = sqlite3.connect('squlite3_mytodo.db')
cursor = connection.cursor()

#Create a database table to store data

cursor.execute('CREATE TABLE tasks ( id INTEGER PRIMARY KEY, task TEXT)')


class todoList:
    def message(self): #to display a simple message in the begining

        print("This is my TODO List")

    def choices(self): 
        # this function will be used to enter the choices for the task we choose to do
        enter = 0
        while (enter !=5):
            enter = input('\n 1. Add a Task \n 2. Edit a Task \n 3. Delete a Task \n 4.View a Task \n 5. Exit the program \n')

            if enter == 1:
                task = raw_input("Enter a Task please here \n")
                cursor.execute('INSERT INTO tasks(task) VALUES(?)', (task, ))
                connection.commit()
                raw_input("Press the Enter key to continue")

            elif enter == 2:
                print("Here is a view of your TODO List \n")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = row [0]
                    task= row [1]
                    print(str(id)+'. '+str(task))
                    row = cursor.fetchone()
                raw_input(" Press the Enter key to continue")

            elif enter == 3:
                print("Enter the id number to edit the task")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = row[0]
                    task = row[1]

                    row = cursor.fetchone()
                number = raw_input('\n')
                task = raw_input("\n Enter id number to edit")
                query = "UPDATE tasks SET task ="+"'"+data+"'"+"WHERE id = "+number

                cursor.execute(query)
                raw_input(" Press the Enter key to continue")
            elif enter == 4:
                print("Enter ID to Delete task \n")
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = row[0]
                    task = row[1]
                    print(str(id)+'. '+str(task))
                    row= cursor.fetchone
                number = raw_input('\n')
                query = "DELETE FROM tasks WHERE id = "+number
                cursor.execute(query)
                raw_input(" Press the Enter key to continue")
            else:
                ("Exit the program")
                sys.exit()
end = todoList()
end.message()
end.choices()




                



