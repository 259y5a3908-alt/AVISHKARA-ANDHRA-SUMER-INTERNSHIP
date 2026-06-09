import sqlite3

# Connect to database
conn = sqlite3.connect("student.csv")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Marks INTEGER
)
""")

# Insert records
cursor.execute("INSERT INTO Student(Name, Marks) VALUES('Fiza', 85)")
cursor.execute("INSERT INTO Student(Name, Marks) VALUES('Ali', 90)")
cursor.execute("INSERT INTO Student(Name, Marks) VALUES('Sara', 78)")

# Save changes
conn.commit()

# Display records
cursor.execute("SELECT * FROM Student")

print("ID\tName\tMarks")
print("-"*20)

for row in cursor.fetchall():
    print(f"{row[0]}\t{row[1]}\t{row[2]}")

# Close connection
conn.close()