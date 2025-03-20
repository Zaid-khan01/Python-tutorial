# mysql connectivity
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Zaidkhan1123",
    database = "mydatabase"
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES")

for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()

