import mysql.connector
from mysql.connector import Error


def create_connection(database=None):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database=database
        )
    except Error as connection_error:
        print(f"There is an error: {connection_error}")
        return
    return mydb
