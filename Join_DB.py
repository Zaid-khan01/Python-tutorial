import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaidkhan1123",
    database="mydatabase"
)

newCursor = conn.cursor()
#
# # ------------------ Clear Existing Data --------------------
# newCursor.execute("DELETE FROM student")
# newCursor.execute("DELETE FROM department")
# conn.commit()  # Commit the delete operation
#
# # ------------------ Insert into Student Table --------------------
# sql = "INSERT INTO student (Id, Name, Dept_id) VALUES (%s, %s, %s)"
# val = [
#     (101, "Zaid khan", 10),
#     (102, "Md Ahmad", 10),
#     (103, "Aman", 11),
#     (104, "Vijay", 12)
# ]
# newCursor.executemany(sql, val)
# conn.commit()  # Commit the insert operation
#
# # ------------------ Insert into Department Table --------------------
# sql = "INSERT INTO department (ID, Name) VALUES (%s, %s)"
# val = [
#     (10, "CSE"),
#     (11, "ME"),
#     (12, "ECE")
# ]
# newCursor.executemany(sql, val)
# conn.commit()  # Commit the insert operation
#
# # ------------------ INNER JOIN Query --------------------
# print("Inner Join of student and department tables:")
# sql = """
#     SELECT student.Name AS student, department.Name AS Dept_id
#     FROM student
#     INNER JOIN department ON student.Dept_id = department.ID
# """
# newCursor.execute(sql)
#
# # Fetch and display the result
# result = newCursor.fetchall()
# for x in result:
#     print(x)
#
# # Clean up
# newCursor.close()
# conn.close()
#
#

# ---------------- Left join ------------------
# print("Left Join of student and department tables:")
# sql = """
#     SELECT student.Name AS student, department.Name AS Dept_id
#     FROM student
#     left JOIN department ON student.Dept_id = department.ID
# """
# newCursor.execute(sql)
#
# # Fetch and display the result
# result = newCursor.fetchall()
# for x in result:
#     print(x)
#
# # Clean up
# newCursor.close()
# conn.close()
#

# ---------------- Right join ------------------
print("Right Join of student and department tables:")
sql = """
    SELECT student.Name AS student, department.Name AS Dept_id
    FROM student
    Right JOIN department ON student.Dept_id = department.ID
"""
newCursor.execute(sql)

# Fetch and display the result
result = newCursor.fetchall()
for x in result:
    print(x)

# Clean up
newCursor.close()
conn.close()
