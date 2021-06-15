import sqlite3
from sqlite3 import Error
from flaskblog.routes import forms

def create_connection(form):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect('forms.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM forms")

        rows = cur.fetchall()
        print(rows)
    except Error as e:
        print(e)

    return conn

def create_connection(form):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('forms.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()