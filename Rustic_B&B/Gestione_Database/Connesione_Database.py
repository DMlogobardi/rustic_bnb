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

#quary for test
def __quary_test__():
  cursor = mydb.cursor()
  cursor.execute("SELECT * FROM utente")
  result = cursor.fetchall()
  return result
