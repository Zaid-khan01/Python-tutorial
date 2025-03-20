import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaidkhan1123",
    database="mydatabase"
)

newCursor = conn.cursor()

# --------------------- Update -----------------------
sql = "update ORDER123 set Name = 'Manish' where Name = 'Rahul'"
newCursor.execute(sql)
conn.commit()   # after commiting name will changed to manish from rahul


sql = "select * from ORDER123"
newCursor.execute(sql)
result = newCursor.fetchall()
for x in result:
    print(x)