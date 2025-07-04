# %%
#!pip install SQLAlchemy==1.4.49 --force-reinstall
#!pip install ipython-sql
#!pip install pymysql psycopg2

# %%
#%load_ext sql

# %%
#%sql mysql+pymysql://root:@Toor001@localhost:3306/edu_institute

# %% [markdown]
# 1. Database Creation and Table Setup (2 Marks)
# 
#     1.1 Create a database named edu_institute. (0.5 Marks)
#     
#     1.2 Within edu_institute, create a table named students (1.5 marks)

# %%
# Importing Python Libraries
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Database Connection Configuration
# Replace 'your_username' and 'your_password' with your MySQL credentials.
DB_USER = 'root'
DB_PASSWORD = '@Toor001'
DB_HOST = 'localhost'
DB_NAME = 'edu_institute'

#Lets establish a connection to the MySQL Server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Server Connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#Function to execute SQL queries
# This function can be used to execute any SQL query that does not return data (e.g., CREATE, INSERT, DROP).
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query executed successfully.")
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()

# Now we will create a function to read data from the database and return it in a structured format.
def read_query_to_dataframe(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return pd.DataFrame(records, columns=columns)
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()

# Then we stablish a connection for the notebook session
# First, connect to the server to create the database
server_conn = create_server_connection(DB_HOST, DB_USER, DB_PASSWORD)

# Then, create the database if it doesn't exist
if server_conn:
    execute_query(server_conn, f"CREATE DATABASE IF NOT EXISTS edu_institute")
    server_conn.close()

# Now, establish a persistent connection to the edu_institute database for the rest of the script
db_conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
print(f"Connection to database edu_institute established.")

# We drop the table first to ensure the script is runnable multiple times without errors.
drop_table_query = "DROP TABLE IF EXISTS students"
execute_query(db_conn, drop_table_query)

create_table_query = """
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender CHAR(1),
    enrollment_date DATE,
    program VARCHAR(50)
);
"""
execute_query(db_conn, create_table_query)

# %% [markdown]
# 2.1  Insert at least 5 records into the students table, with diverse names, ages, genders, enrolment dates, and programs.
# Ensure at least one student is enrolled in "Data Science". (2 Marks)

# %%
# Insert at least 5 records into the students table
insert_data_query = """
INSERT INTO students (student_id, name, age, gender, enrollment_date, program) VALUES
(1, 'Seth Rollins', 22, 'M', '2022-10-01', 'Architecture'),
(2, 'Bobby Lashley', 23, 'M', '2020-08-30', 'Data Science'),
(3, 'Charlotte Flaire', 21, 'F', '2022-02-20', 'International Relations'),
(4, 'Becky Lynch', 24, 'F', '2019-05-10', 'Data Science'),
(5, 'Randy Orton', 25, 'M', '2023-01-15', 'Zoology'),
(6, 'Rhea Ripley', 20, 'F', '2021-09-01', 'Sports Science');
"""
execute_query(db_conn, insert_data_query)

# %% [markdown]
# 3.1  Write a query to select all columns for all students in the "Data Science" program

# %%
query_ds_students = "SELECT * FROM students WHERE program = 'Data Science';"
ds_students_df = read_query_to_dataframe(db_conn, query_ds_students)
print("Students in the 'Data Science' program:")
display(ds_students_df)

# %% [markdown]
# 3.2 Write a query to find the total number of students and display it as Total Students

# %%
query_total_students = "SELECT COUNT(*) AS 'Total Students' FROM students;"
total_students_df = read_query_to_dataframe(db_conn, query_total_students)
print("Total number of students:")
display(total_students_df)

# %% [markdown]
# 4.1 Use an appropriate function to display the current date in a column named Today's Date

# %%
query_current_date = "SELECT CURRENT_DATE() AS `Today's Date`;"
current_date_df = read_query_to_dataframe(db_conn, query_current_date)
print("Today's Date:")
display(current_date_df)

# %% [markdown]
# 4.2  Write a query to select the student names and their enrolment dates, but display the name column in uppercase

# %%
query_uppercase_names = "SELECT UPPER(name) AS student_name, enrollment_date FROM students;"
uppercase_df = read_query_to_dataframe(db_conn, query_uppercase_names)
print("Student names in uppercase:")
display(uppercase_df)

# %% [markdown]
# 5.1 Write a query to count the number of students in each program and display the results in descending order of count

# %%
query_program_count = """
SELECT program, COUNT(*) AS 'Number of Students'
FROM students
GROUP BY program
ORDER BY `Number of Students` DESC;
"""
program_count_df = read_query_to_dataframe(db_conn, query_program_count)
print("Number of students per program:")
display(program_count_df)

# %% [markdown]
# 5.2 Write a query to find the youngest student's name and age

# %%
query_youngest_student = "SELECT name, age FROM students ORDER BY age ASC LIMIT 1;"
youngest_student_df = read_query_to_dataframe(db_conn, query_youngest_student)
print("Youngest student:")
display(youngest_student_df)

if db_conn and db_conn.is_connected():
    db_conn.close()
    print("Database connection closed.")


