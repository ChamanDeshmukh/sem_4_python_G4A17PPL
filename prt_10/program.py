import mysql.connector
from time import sleep

mydb = mysql.connector.connect(host="localhost",user="zeref",password="7788",database="student",buffered=True)

cursor = mydb.cursor()
print("Creating table details...")
cursor.execute("CREATE TABLE details(name varchar(255), roll_no varchar(255), phone_no varchar(255))")

print("Creating table details...")
cursor.execute("SHOW TABLES")
print("Table Created.")

print("Inserting values...")
sleep(2)
cmd = "INSERT INTO details VALUES (%s, %s, %s)"
val = [
        ("Aryan Pateriya","210031101611001","7000193823"),
        ("Bhavya Jalap","210031101611002","7877622610"), 
        ("Chaman Deshmukh","210031101611003","7694943420"),
        ("Shubham Kumar","210031101611004","7889244780")
      ]
cursor.executemany(cmd,val)
mydb.commit()

print("Done")
cursor.execute("SELECT * FROM details")

print("Inserted Values are :")
output = cursor.fetchall()
for row in output:
    print(row)

print("\n Setting roll_no to NOT NULL")
cursor.execute("ALTER TABLE details MODIFY roll_no varchar(255) NOT NULL")
cursor.execute("DESC details")

output = cursor.fetchall()
for row in output:
    print(row)
print("Done")

print("Deleting the Entry of Shubham")
cursor.execute("DELETE FROM details WHERE name='Shubham Kumar'")
mydb.commit()
print("Done :")

cursor.execute("SELECT * FROM details")
output = cursor.fetchall()
for row in output:
    print(row)
