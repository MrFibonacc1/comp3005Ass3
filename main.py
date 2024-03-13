#Huzaifa Rehan
#ID:101-266-460
#Comp 3005 A3

#Import functions and code from other files/directories
from database.postgres import create_connection, close_connection
from database.functions import getAllStudents, addStudent, updateStudentEmail, deleteStudent

#You can replace these defualt values which your database details
db_name = ""
db_user = ""
db_password = ""
db_host = ""
db_port = ""

#This just connects to the database
connection = create_connection(db_name, db_user, db_password, db_host, db_port)

#Ask for user input and choice
#Depending on their choice, it will call the according function
inp = 0
while inp!=5:
    inp = int(input("Enter 1 to retrieve and display all students \nEnter 2 to add a student \nEnter 3 to update a student email address \nEnter 4 to delete a student\nEnter 5 to exit\n"))

    if inp == 1:
        print("Getting all students")
        students = getAllStudents(connection)
        for i in students:
            print(i)

    elif inp == 2:
        firstName = input("What is the first name of the student\n")
        lastName = input("What is the last name of the student\n")
        email = input("What is the email of the student\n")
        enrollDate = input("What is the enrollment date of the student in the format year/month/day\n")
        print("Adding Student")
        addStudent(connection,firstName,lastName,email,enrollDate)
        
    elif inp == 3:
        id = int(input("What is the id of the student\n"))
        email = input("What is the new email of the student\n")
        print("Changing Student's Email")
        updateStudentEmail(connection,id,email)
        
    elif inp == 4:
        print("Deleting Student")
        id = int(input("Whats the student ID\n"))
        deleteStudent(connection,id)

#This closes the conenction to the database when the program is finished
close_connection(connection)
