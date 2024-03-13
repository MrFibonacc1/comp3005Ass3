
#This is the function that connects to the database and gets all the students
def getAllStudents(connection):
    try:
        #The query
        query = "SELECT * FROM students;"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed succesfully")
        #Fetch all students
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"The error '{e}' occurred")
        return None

#This function uses the details to create a new student in the database
def addStudent(connection, first_name, last_name, email, enrollment_date):
    try:
        query = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Student added successfully")
    except Exception as e:
        print(f"Error while adding student: {e}")

#This function gets the student id and changes their email to the new given email
def updateStudentEmail(connection, student_id, new_email):
    try:
        query = f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id}"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Email updated successfully")
    except Exception as e:
        print(f"Error while updating student email: {e}")

#This function gets the student id and deletes the student
def deleteStudent(connection, student_id):
    try:
        query = f"DELETE FROM students WHERE student_id = {student_id}"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Student deleted successfully")
    except Exception as e:
        print(f"Error while deleting student: {e}")

