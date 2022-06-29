import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bd_python"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE bd_python")
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

#mycursor.execute("CREATE TABLE etudiant (nom VARCHAR(50), postnom VARCHAR(50), prenom VARCHAR(50), addresse VARCHAR(255))")

sql = "INSERT INTO etudiant (nom, postnom, prenom, addresse) VALUES (%s, %s, %s, %s)"
val = ("Baraka", "Bigega", "Espoir", "Goma")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")