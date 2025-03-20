import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaidkhan1123",
    database="mydatabase"
)

newCursor = conn.cursor()

# ------------------- Delete ----------------------
print("Deleting a particular tuple whose name is 'Zaid khan'")
del_tuple = "Delete from ORDER123 where Name = %s"
del_val = ("Zaid khan",)


newCursor.execute(del_tuple, del_val)

newCursor.execute("Select* from ORDER123")
result = newCursor.fetchall()
for x in result:
    print(x)

conn.commit()