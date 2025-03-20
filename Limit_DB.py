import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaidkhan1123",
    database="mydatabase"
)

newCursor = conn.cursor()

# -------------------- Limit ---------------------
# limit just print the particular data upto given limit

newCursor.execute("Select * from ORDER123 limit 2")

result = newCursor.fetchall()
for x in result:
    print(x)


# ------------- using Offset in limit -------------------
print("After using offset - ")
newCursor.execute("Select * from ORDER123 limit 3 offset 1")

result = newCursor.fetchall()
for x in result:
    print(x)
