import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def connect_database():
    connection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME

    )

    if connection.is_connected():
        print("connected to database")

    return connection

def cursor(connection):
    cursor = connection.cursor()

    return cursor

def execute_cursor(cursor,query,values = None):
    if values:
        cursor.execute(query,values)
    else:
        cursor.execute(query)

def close_cursor(cursor):
    cursor.close()

def close_connection(connection):
    connection.close()

