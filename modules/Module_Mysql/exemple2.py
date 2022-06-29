import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "python"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE python")
#mycursor.execute("CREATE TABLE etudiant(id INT, nom VARCHAR(50))")
req = "INSERT into etudiant(id, nom) VALUES(%s, %s)"
donnee = (1, "SIWA")
mycursor.execute(req, donnee)

mydb.commit()