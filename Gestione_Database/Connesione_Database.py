import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port = "3306",
  user="root",
  password="",
  database = "bnb"
)

def __controllo_utent__(campi):
    cursor = mydb.cursor() 
    quary = "SELECT utente.admin FROM utente WHERE utente.username = %s and utente.password = %s"
    
    try:
        cursor.execute(quary, campi)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)

def __insert_utente__(utent):
    cursor = mydb.cursor()
    quary = "INSERT INTO utente (username, password, n_c, data_nascita, gender) VALUES (%s, %s, %s, %s, %s)"
    
    try:
        cursor.execute(quary, utent)
        mydb.commit()
        return 1
    except Exception as e:
        return e
