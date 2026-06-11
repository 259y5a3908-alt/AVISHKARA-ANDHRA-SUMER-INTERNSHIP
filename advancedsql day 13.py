import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create Department Table
cursor.execute("""
CREATE TABLE Departments(
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
)
""")

# Create Employee Table
cursor.execute("""
CREATE TABLE Employees(
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    dept_id INTEGER,
    salary INTEGER,
    experience INTEGER
)
""")

# Insert Departments
departments = [
    (1, "IT"),
    (2, "HR"),
    (3, "Finance"),
    (4, "Marketing")
]

cursor.executemany(
    "INSERT INTO Departments VALUES (?,?)",
    departments
)

# Insert Employees
employees = [
    (101, "Rahul", 1, 60000, 3),
    (102, "Priya", 2, 45000, 2),
    (103, "Kiran", 1, 75000, 5),
    (104, "Sneha", 3, 80000, 6),
    (105, "Arjun", 4, 55000, 4),
    (106, "Meena", 3, 90000, 7),
    (107, "Vikram", 1, 65000, 4)
]

cursor.executemany(
    "INSERT INTO Employees VALUES (?,?,?,?,?)",
    employees
)

conn.commit()

# Advanced SQL Query
query = """
SELECT
    d.dept_name,
    COUNT(e.emp_id) AS total_employees,
    AVG(e.salary) AS average_salary,
    MAX(e.salary) AS highest_salary,
    MIN(e.salary) AS lowest_salary
FROM Employees e
INNER JOIN Departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING AVG(e.salary) > 50000
"""

df = pd.read_sql_query(query, conn)

print("\n===== ADVANCED SQL REPORT =====\n")
print(df)

conn.close()