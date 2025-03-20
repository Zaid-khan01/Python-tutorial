# mysql connectivity
import mysql.connector
# from datetime import datetime
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Zaidkhan1123",
    database = "mydatabase"
)

mycursor = conn.cursor()
# ---------------------- CREATE -------------------------
# create table in database - "mydatabase"
# mycursor.execute("create table CSE2(Sr_no int primary key, Name varchar(20), Address varchar(30), Age int, DOB date)")


# ----------------------- INSERT ------------------------------
# sql = "Insert into CSE2 values(%s, %s, %s, %s, %s)"
# val = (61, "Zaid khan", "Ashok nagar", 20, datetime(2005, 12, 23))
# val2 = (62, "Md Ahmad raza khan", "Janakpuri", 20, datetime(2004, 2, 14))
# mycursor.execute(sql,val2)
#
# conn.commit()
# print(mycursor.rowcount, "record inserted.")
# conn.commit()
# -------------------------- SELECT ------------------------------
mycursor.execute("Select * from CSE2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# if i have to select name, address from CSE2
mycursor.execute("Select Name, Age from CSE2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

