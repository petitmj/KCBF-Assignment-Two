# KCBF-Assignment-Two
# edu-institute-sql-project

**Project Description:** This repository contains a Jupyter Notebook demonstrating basic SQL operations, including database creation, table design, data insertion, and querying.  It's designed as an introductory learning exercise for SQL fundamentals.

**Author:** [petitmj] 

**Date Created:** June 26, 2025

## Table of Contents

1.  [Setup](#setup)
2.  [Running the Notebook](#running-the-notebook)
3.  [SQL Queries Demonstrated](#sql-queries-demonstrated)
4.  [Next Steps](#next-steps)

## Setup

*   **Prerequisites:**
    *   Python 3.11.12 (or later)
    *   MySQL database server (locally or remotely)
    *   `mysql-connector-python` and `pandas` Python packages installed:  `pip install mysql-connector-python pandas`

## Running the Notebook

1.  **Open in Jupyter:** Open the `SQL_Assignment.ipynb` file in a Jupyter Notebook environment.
2.  **Execute Cells:** Follow the instructions within the notebook cells to create the database, table, insert data, and run SQL queries. 

## SQL Queries Demonstrated

The notebook demonstrates the following SQL operations:

*   Creating a MySQL database (`student_demo`)
*   Creating a `students` table with auto-incrementing ID, name, age, and grade columns.
*   Inserting sample student data into the table.
*   Executing queries to retrieve specific information from the table (e.g., finding the youngest student or all students with an 'A' grade).

Specifically, the notebook uses these queries:

*   `CREATE DATABASE IF NOT EXISTS student_demo;`
*   `USE student_demo;`
*   `CREATE TABLE IF NOT EXISTS students (...)`
*   `INSERT INTO students (...) VALUES (...);`
*   `SELECT MIN(name) FROM students WHERE age = (SELECT MIN(age) FROM students);`
*   `SELECT * FROM students WHERE age = (SELECT MIN(age) FROM students);`

## Next Steps

*   **Experiment with different queries:** Modify the SQL queries to explore other data retrieval and manipulation techniques.
*   **Add more complex tables and relationships:** Extend the database schema to include additional tables and relationships between them.
*   **Implement error handling:** Add robust error handling to your Python code to handle potential issues during database interactions.



