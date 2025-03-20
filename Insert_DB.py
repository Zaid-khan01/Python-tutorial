import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaidkhan1123",
    database="mydatabase"
)

newCursor = conn.cursor()

# newCursor.execute("CREATE TABLE ORDER123 (Order_id INT PRIMARY KEY, Name VARCHAR(20), Address VARCHAR(20))")

sql = "insert into ORDER123 values(%s, %s, %s)"
val = [
    (101, "Zaid khan", "CSE"),
    (102, "Md ahmad", "CSE"),
    (103, "Rahul", "ME"),
    (104, "Sonu", "ECE")
]

# ------------------ Select Whole Table -------------------
newCursor.executemany(sql, val)
newCursor.execute("Select * from ORDER123")
result = newCursor.fetchall()

for x in result:
    print(x)

conn.commit()
# -------------------------- WHERE -------------------------
# print("Selecting a particular tuple")
# sql = "select * from ORDER123 where Name = 'Zaid khan'"
# newCursor.execute(sql)
#
# result = newCursor.fetchall()
# for x in result:
#     print(x)


