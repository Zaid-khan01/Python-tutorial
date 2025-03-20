import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaidkhan1123",
    database="mydatabase"
)

newCursor = conn.cursor()

# --------------------- Order -----------------------
print("Order the database in either ascending or descending")
print("First sort it in ascending order")
sql = "select * from ORDER123 order by Name"
newCursor.execute(sql)

result = newCursor.fetchall()
for x in result:
    print(x)


print("Sort it in descending order")
sql = "select * from ORDER123 order by name desc"
newCursor.execute(sql)

result = newCursor.fetchall()
for x in result:
    print(x)