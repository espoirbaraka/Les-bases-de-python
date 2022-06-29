import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bd_python"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE section (id varchar(255) default uuid(), designation VARCHAR(50))")