import mysql.connector
from mysql.connector import cursor

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
    
def __add_prezzo__(prezzo):
    cursor = mydb.cursor()
    quary = "UPDATE offerte_prezzi SET prezzo_offerta = %s WHERE offerte_prezzi.id = 1"
        
    try:
        cursor.execute(quary, prezzo)
        mydb.commit()
        return 1
    except Exception as e:
        return e
    
def __guadagno__():
    cursor = mydb.cursor()
    quary = "SELECT prenotazioni.cost FROM prenotazioni"
    
    try:
        cursor.execute(quary)
        result = cursor.fetchall()
        return result.__str__()
    except Exception as e:
        return e
        
def __add_Discount__(offerta):
    cursor = mydb.cursor()
    quary = "INSERT INTO offerte_prezzi (data_in, data_out, prezzo_offerta) VALUES (%s, %s, %s)"
    
    try:
        cursor.execute(quary, offerta)
        mydb.commit()
        return 1
    except Exception as e:
        return e

def __discount__():
    cursor = mydb.cursor()
    quary = "SELECT * FROM offerte_prezzi WHERE offerte_prezzi.id != 1"
    
    try:
        cursor.execute(quary)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return e
    
def __prenotation__():
    cursor = mydb.cursor()
    quary = "SELECT * FROM prenotazioni"
    
    try:
        cursor.execute(quary)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return e
    
def __delete__(id):
    cursor = mydb.cursor()
    quary = "DELETE FROM offerte_prezzi WHERE offerte_prezzi.id = %s"
    
    try:
        cursor.execute(quary, id)
        mydb.commit()
        return 1
    except Exception as e:
        return e
    
def __mod__(mod):
    cursor = mydb.cursor()
    quary = "UPDATE offerte_prezzi SET data_in = %s, data_out = %s, prezzo_offerta = %s WHERE  offerte_prezzi.id = %s"
    
    try:
        cursor.execute(quary, mod)
        mydb.commit()
        return 1
    except Exception as e:
        return e
    
def __utent__(campi):
    cursor = mydb.cursor() 
    quary = "SELECT utente.id FROM utente WHERE utente.username = %s"
    
    try:
        cursor.execute(quary, campi)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        
def __add_prenotation__(campi):
    cursor = mydb.cursor()
    quary = "INSERT INTO prenotazioni (fk_utente, fk_offerte, data_checkin, data_checkout, cost) VALUES (%s, %s, %s, %s, %s)" 
     
    try:
        cursor.execute(quary, campi)
        mydb.commit()
        return 1
    except Exception as e:
        return e 
def __utent_prenotation__(utent):
    cursor = mydb.cursor()
    quary = "SELECT * FROM prenotazioni JOIN utente ON utente.id = prenotazioni.fk_utente WHERE utente.username = %s"
    
    try:
        cursor.execute(quary, utent)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return e