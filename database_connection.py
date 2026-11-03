import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def connect_database():      #connecting to database
    connection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME

    )

    if connection.is_connected():
        print("connected to database")

    return connection

def cursor(connection):     #creating a cursor 
    cursor = connection.cursor()

    return cursor

def execute_cursor(cursor,query,values = None):  #executing the cursor query with its values
    if values:
        cursor.execute(query,values)
    else:
        cursor.execute(query)
def commit(connection):         #finalizing and commiting the query
    connection.commit()

def close_cursor(cursor):      #closing cursor 
    cursor.close()

def close_connection(connection):  #closing connection after use
    connection.close()

def connection_n_cursor():
    connection = connect_database()
    cursor = connection.cursor()

    return cursor

def everything(query,values):
    connection = connect_database()
    cursor = cursor(connection)
    execute_cursor(query,values)
    commit(connection)
    close_cursor(cursor)
    close_connection(connection)