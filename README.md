This assignment for comp 3005 involved creating a simple application that connects to postgres and allows the user to do basic CRUD operations on the database.

Step 1:
To setup this code, clone the github code and install the module psycopg2 by running the following command:

pip3 install psycopg2

Step 2:
Setup the database by using the schema and fill it with data

Use this sql query to create the table:

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

And then inject data by using this data:

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');



Step 3:
Head to the main.py and fill in the postgres connection details using your own postgres database details. 

Step 4:
You should be able to run the code by running this command:

python3 main.py


VIDEO LINK:

https://youtu.be/8FY_GOQ6lD4

