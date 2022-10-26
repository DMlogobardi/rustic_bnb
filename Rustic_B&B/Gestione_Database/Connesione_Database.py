from select import select
from sqlite3 import Cursor, connect
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port = "3306",
  user="root",
  password="",
  database = "bnb"
)

cursor = mydb.cursor()

#quary for test
cursor.execute("SELECT * FROM utente")

result = cursor.fetchall()

for x in result:
  print(x)
